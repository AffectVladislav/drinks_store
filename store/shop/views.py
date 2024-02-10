from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .paginator import paginator

def store(request):
    products = Product.objects.filter(available=True).order_by('?')
    context = {'page_obj': paginator(request, products, 6),
               'other_product': paginator(request, products, 3)}
    return render(request, 'shop/product/main_page.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, Slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})
