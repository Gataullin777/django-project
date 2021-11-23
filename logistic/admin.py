from django.contrib import admin
from .models import Stock, Product


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_prupal = 'Продукты'

    list_display = ['title', 'description']
