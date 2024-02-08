from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .paginator import paginator

def store(request):
    products = Product.objects.filter(available=True)
    context = {'page_obj': paginator(request, products, 6)}
    return render(request, 'shop/product/main_page.html', context)