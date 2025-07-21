# views.py
from rest_framework import viewsets
from .models import ProductType, Product, ProductAttribute, ProductAttributeValue
from .serializers import (
    ProductTypeSerializer,
    ProductSerializer,
    ProductCreateSerializer,
    ProductAttributeSerializer,
    ProductAttributeValueSerializer,
)
from .permissions import IsAdminOrReadOnly
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('attribute_values__attribute', 'product_type').all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductCreateSerializer
        return ProductSerializer


class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductAttributeValueViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributeValue.objects.select_related('attribute', 'product').all()
    serializer_class = ProductAttributeValueSerializer
    permission_classes = [IsAdminOrReadOnly]
