from django_filters import rest_framework as filters

from logistic.models import Product


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter, filters.NumberFilter):
    pass

class StocksFilter(filters.FilterSet):
    product = CharFilterInFilter(field_name='positions__product', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['product']
