from django.urls import path
from .views import store

app_name = 'shop'

urlpatterns = [
    path('', store, name='home'),
]
