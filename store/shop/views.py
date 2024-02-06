from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

def index(request):
    t = render_to_string('templates/shop/base.html')
    return HttpResponse(t)