from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from .models import Product, Category, HeatLevel, Brand, ProductReview
from .forms import ProductForm, ProductReviewForm
from checkout.models import Order


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    brand = None
    heat_level = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            # Allow sorting the products
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'brand':
                sortkey = 'brand__name'
            if sortkey == 'heat_level':
                sortkey = 'heat_level__heat_order'

            if 'direction' in request.GET:
                # set the direction of the sorting
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            # Allow filter by category
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            # Allow filter by brand
            brand = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brand)
            brand = Brand.objects.filter(name__in=brand)

        if 'heat_level' in request.GET:
            # allow filter by heat level
            heat_level = request.GET['heat_level'].split(',')
            products = products.filter(heat_level__name__in=heat_level)
            heat_level = HeatLevel.objects.filter(name__in=heat_level)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # messages to report that there was nothing searched
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # queries to allow searching for a product
            # i for case insensitivity
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query) | Q(heat_level__name__iexact=query) | Q(brand__name__icontains=query)  # noqa
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brands': brand,
        'current_heat': heat_level,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to show the full detail of an individual product
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.product_reviews.all()
    filter_reviews = ProductReview.objects.filter(product=product)
    avg_rating = filter_reviews.aggregate(Avg('rating'))['rating__avg']

    context = {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    A view to allow adding products
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        # request.FILES to capture submitted image
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # if the form is valid, save and send success message
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    A view to allow editing products
    """
    # prefill the form with the current product details
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    A view to handle deleting products
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_superuser:
        if request.method == 'POST':
            product.delete()
            messages.success(request, 'Product deleted!')
            return redirect(reverse('products'))

        return render(
            request,
            'products/delete_product.html', {'product': product})
    else:
        messages.error(request, 'Only store owners can do that')
        return redirect(reverse('products'))


@login_required
def review_product(request, product_id):
    """
    A view to collect product reviews from the user
    The user must be logged in and have ordered the product before
    """
    product = get_object_or_404(Product, pk=product_id)
    # Only allow the user to rate a product once
    if ProductReview.objects.filter(product=product,
                                    reviewer=request.user).exists():
        messages.error(request, 'Sorry, you can only rate a product once')
        return redirect('product_detail', product_id=product_id)
    else:
        # Determine if the user is authenticated
        if request.user.is_authenticated and not isinstance(request.user,
                                                            AnonymousUser):
            # Check that the user has ordered the product before
            if Order.objects.filter(email=request.user.email,
               lineitems__product=product).exists():
                if request.method == 'POST':
                    form = ProductReviewForm(request.POST)
                    if form.is_valid():
                        review = form.save(commit=False)
                        review.product = product
                        review.reviewer = request.user
                        review.save()
                        messages.success(
                            request, 'Successfully Added your review!')
                        return redirect('product_detail',
                                        product_id=product_id)
                else:
                    form = ProductReviewForm()
            else:
                messages.error(
                    request,
                    'You must have ordered this product to write a review')
                return redirect('product_detail', product_id=product_id)
        else:
            messages.error(request,
                           'Sorry, you must be logged in to review products')
            return redirect('account_login')

    template = 'products/review_product.html'
    context = {
        'form': form,
        'product': product
        }
    return render(request, template, context)


@login_required
def edit_product_review(request, review_id):
    """
    A view to allow the user to edit their own reviews
    """
    review = get_object_or_404(ProductReview, id=review_id)

    # Check if the current user is the owner of the review
    if request.user == review.reviewer:
        # If the request is post, save the form
        if request.method == 'POST':
            form = ProductReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully added your review!')
                return redirect('product_detail', product_id=review.product.id)
        else:
            # Else, render the form with the current review details
            form = ProductReviewForm(instance=review)
        # Redirect to the edit_product_review template
        context = {'form': form, 'review': review}
        return render(request, 'products/edit_product_review.html', context)
    else:
        # Error if the user does not own that review
        messages.error(request, 'You can only edit your own review')
        return redirect('product_detail', product_id=review.product.id)


@login_required
def delete_product_review(request, review_id):
    """
    A review to delete a product review
    The user must be logged in and own the review to delete it
    """
    review = get_object_or_404(ProductReview, id=review_id)

    # Check if the current user is the owner of the review
    if request.user == review.reviewer:
        if request.method == 'POST':
            # If the user confirms deletion, delete the review
            review.delete()
            messages.success(request, 'Successfully deleted your review')
            return redirect('product_detail', product_id=review.product.id)

        # Render the confirmation template
        context = {'review': review}
        return render(request, 'products/delete_review.html', context)
    else:
        # If the user is not the owner of the review,
        # redirect them back to the product detail page
        messages.error(request, 'You can only delete your own review')
        return redirect('product_detail', product_id=review.product.id)
