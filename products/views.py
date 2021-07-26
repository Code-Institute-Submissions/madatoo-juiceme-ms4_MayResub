from django.shortcuts import render
from .models import Product

# view to display all product


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)
