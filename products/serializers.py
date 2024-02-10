from django.conf import settings
from rest_framework import serializers

from products.models import (
    CategoryModel,
    ProductModel,
    ProductImageModel,
    ProductPropertiesModel,
)


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImageModel
        fields = ("image_url",)

    def get_image_url(self, obj):
        return settings.BASE_URL + obj.image.url


class ProductModelSerializer(serializers.ModelSerializer):
    additional_images = serializers.ListField(
        child=serializers.ImageField(), required=False
    )
    high = serializers.FloatField()
    width = serializers.FloatField()
    length = serializers.FloatField()
    weight = serializers.FloatField()

    class Meta:
        model = ProductModel
        fields = (
            "name",
            "price",
            "main_image",
            "categories",
            "description",
            "additional_images",
            "high",
            "width",
            "length",
            "weight",
        )


class ProductListSerializer(serializers.ModelSerializer):
    categories = CategoryModelSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = ("id", "name", "price", "main_image", "categories")


class ProductPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPropertiesModel
        fields = ("length", "width", "high", "weight")


class ProductDetailSerializer(serializers.ModelSerializer):
    categories = CategoryModelSerializer(many=True)
    additional_images = serializers.SerializerMethodField()
    properties = ProductPropertiesSerializer()

    class Meta:
        model = ProductModel
        fields = (
            "name",
            "description",
            "price",
            "main_image",
            "categories",
            "additional_images",
            "properties",
        )

    def get_additional_images(self, obj):
        additional_images = ProductImageSerializer(
            obj.product_images.all(), many=True
        ).data
        return additional_images
