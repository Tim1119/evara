# serializers.py
from rest_framework import serializers
from .models import ProductType, Product, ProductAttribute, ProductAttributeValue


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ['id', 'name']


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    attribute = ProductAttributeSerializer()

    class Meta:
        model = ProductAttributeValue
        fields = ['id', 'attribute', 'value']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()
    attribute_values = ProductAttributeValueSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'product_type', 'attribute_values']


# Create-only version for admin use
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'product_type']
