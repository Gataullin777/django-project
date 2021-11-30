from django.contrib import admin
from .models import Stock, Product, StockProduct


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 0




@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_prupal = 'Продукты'

    # list_display = ['id', 'address',]

    def __str__(self):
        return f'{self.id}, {self.address}'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_prupal = 'Продукты'

    list_display = ['id','title', 'description']
