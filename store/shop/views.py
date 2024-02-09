from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .paginator import paginator

def store(request):
    products = Product.objects.filter(available=True).order_by('?')
    context = {'page_obj': paginator(request, products, 6)}
    return render(request, 'shop/product/main_page.html', context)

def other_products(request):
    context = {'other_prod': paginator(request, products, 3)}
    return render(request, 'shop/product/main_page.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, 'shop/product/detail.html', {'product': product})