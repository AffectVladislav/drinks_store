from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', admin.site.urls),
]
