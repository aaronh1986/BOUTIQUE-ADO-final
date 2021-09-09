from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view show all products including searching and sorting """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)