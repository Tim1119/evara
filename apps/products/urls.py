# urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    ProductTypeViewSet,
    ProductViewSet,
    ProductAttributeViewSet,
    ProductAttributeValueViewSet
)

router = DefaultRouter()
router.register(r'product-types', ProductTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-attributes', ProductAttributeViewSet)
router.register(r'attribute-values', ProductAttributeValueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
