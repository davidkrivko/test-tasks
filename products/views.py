from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from products.models import (
    ProductModel,
    CategoryModel,
    ProductImageModel,
    ProductPropertiesModel,
)
from products.serializers import (
    ProductListSerializer,
    ProductModelSerializer,
    CategoryModelSerializer,
    ProductDetailSerializer,
)


class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination
    page_size = 10
    queryset = ProductModel.objects.all().prefetch_related("categories")


class ProductCreateApiView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        additional_images = serializer.validated_data.pop("additional_images", [])

        high = serializer.validated_data.pop("high")
        width = serializer.validated_data.pop("width")
        length = serializer.validated_data.pop("length")
        weight = serializer.validated_data.pop("weight")

        product = self.perform_create(serializer)

        ProductPropertiesModel.objects.create(
            product=product,
            high=high,
            width=width,
            length=length,
            weight=weight
        )

        for image in additional_images:
            ProductImageModel.objects.create(product=product, image=image)

        return Response({"detail": "Product was created!"}, status=201)


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        serializer.is_valid(raise_exception=True)
        additional_images = serializer.validated_data.pop("additional_images")

        self.perform_update(serializer)

        if additional_images:
            ProductImageModel.objects.filter(product=instance).delete()

            for image in additional_images:
                ProductImageModel.objects.create(product=instance, image=image)

        return Response({"detail": "Product was updated!"}, status=202)


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = ProductModel.objects.all().prefetch_related("categories")
    serializer_class = ProductDetailSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer
