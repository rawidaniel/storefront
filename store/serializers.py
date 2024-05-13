from rest_framework import serializers
from decimal import Decimal
from .models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
    
    products_count = serializers.IntegerField(read_only=True)
    # products_count = serializers.SerializerMethodField(method_name='get_products_count')

    # def get_products_count(self, obj):
    #     return obj.products.count()

  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','description', 'slug', 'inventory', 'unit_price','price_with_tax', 'collection']
    
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name='collection-detail'
    # )
    # collection = CollectionSerializer()
    # collection = serializers.StringRelatedField()
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset= Collection.objects.all()
    # )

    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.1)