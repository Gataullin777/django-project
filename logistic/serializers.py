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
        fields = ['address', 'positions',]


    class Meta:
        model = Stock
        fields = ['address', 'positions',]




    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock

    def update(self, instance, validated_data):

        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        stock_id = stock.id
        print()
        available_product_id_in_stock_list = [product.product_id for product in StockProduct.objects.filter(stock_id=stock_id)]
        print()

        for position in positions:
            print()
            product_id = position['product'].id
            print()
            if product_id in available_product_id_in_stock_list:
                stock_instance = StockProduct.objects.get(product_id)
                print()
                stock_instance.update(stock=stock, **position)

        return stock
