from django.core.paginator import Paginator

def paginator(request, products, items_on_page):
    paginator = Paginator(products, items_on_page)
    page_number = request.GET.get('page')

    return paginator.get_page(page_number)