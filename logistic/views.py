from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters import rest_framework as rest_filters
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
# from logistic.service import StocksFilter


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['title', 'description']




class StockViewSet(ModelViewSet):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['product']