from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, HeatLevel, Brand

# Create your views here.

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
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # queries to allow searching for a product
            # i for case insensitivity
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query) | Q(heat_level__name__iexact=query) | Q(brand__name__icontains=query) # noqa
            products = products.filter(queries) 

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories' : categories,
        'current_brands' : brand,
        'current_heat' : heat_level,
        'current_sorting' : current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to show the full detail of an individual product
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)