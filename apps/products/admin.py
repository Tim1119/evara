from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ProductType, Product, ProductAttribute, ProductAttributeValue

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'price', 'created_at')
    list_filter = ('product_type', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    autocomplete_fields = ('product_type',)


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'created_at')
    list_filter = ('product_type',)
    search_fields = ('name',)
    ordering = ('-created_at',)


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value', 'product')
    list_filter = ('attribute__product_type',)
    search_fields = ('value', 'attribute__name', 'product__name')
    autocomplete_fields = ('product', 'attribute')
