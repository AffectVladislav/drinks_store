from django.contrib import admin
from .models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'pub_date', 'available','updated', 'price', 'old_price']
    list_filter = ('price', 'name', 'pub_date', 'updated')
    search_fields = ['name']
    list_editable = ['price', 'old_price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    list_filter = ['name']
    search_fields = ['name']