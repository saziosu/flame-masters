from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product



def view_cart(request):
    """
    view to render the cart contents on the front end
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    View to handle adding products to the shopping cart
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        # if this item is already in the cart, add to it
        cart[item_id] += quantity
    else:
        # else, add the quantity
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def modify_cart(request, item_id):
    """
    View to handle modifying the quantity of an item in the cart
    """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    View to remove items from the cart
    """

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)