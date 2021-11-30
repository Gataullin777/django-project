from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description',]

class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price',]



class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions',]

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        available_product_id_in_stock_list = [product.product_id for product in stock.positions.all()]
        for position in positions:
            product_id = position['product'].id

            if product_id in available_product_id_in_stock_list:
                product_data = stock.positions.filter(product_id=product_id)

                product_data.update(stock=stock, **position)

            elif product_id not in available_product_id_in_stock_list:
                stock.positions.create(stock=stock, **position)

        return stock
