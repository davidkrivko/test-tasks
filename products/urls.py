from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import (
    CategoryModelViewSet,
    ProductListApiView,
    ProductCreateApiView,
    ProductDetailApiView, ProductUpdateApiView,
)


router = DefaultRouter()
router.register(r"categories", CategoryModelViewSet, basename="category")


urlpatterns = [
    path("", include(router.urls)),

    # PRODUCTS
    path(
        "products/",
        ProductListApiView.as_view(),
        name="product-list"
    ),
    path(
        "products/update/<int:pk>/",
        ProductUpdateApiView.as_view(),
        name="product-update"
    ),
    path(
        "products/create/",
        ProductCreateApiView.as_view(),
        name="product-create"
    ),
    path(
        "products/detail/<int:pk>/",
        ProductDetailApiView.as_view(),
        name="product-detail"
    ),
]

app_name = "products"
