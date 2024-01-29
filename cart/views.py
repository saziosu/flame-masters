from django.shortcuts import render


def view_cart(request):
    """
    view to render the cart contents on the front end
    """
    return render(request, 'cart/cart.html')