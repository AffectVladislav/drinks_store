from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя категории')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слизь к категории')

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название продукта')
    description = models.TextField(blank=True, verbose_name='Описание продукта')
    slug = models.SlugField(max_length=50)
    image = models.ImageField(blank=True, upload_to='product', verbose_name='Изображение')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    old_price = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='Старая цена')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-pub_date']),
        ]

    def __str__(self):
        return self.name