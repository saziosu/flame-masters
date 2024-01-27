from django.shortcuts import render
from . import Product

# Create your views here.
from django.shortcuts import render


def all_products(request):
    """
    View to show all products
    """
    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, 'products/products.html', context)