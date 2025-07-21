# filters.py
import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    product_type = django_filters.CharFilter(field_name='product_type__name', lookup_expr='iexact')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['product_type', 'min_price', 'max_price']
