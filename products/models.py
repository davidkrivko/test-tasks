from django.db import models

from products.media_path import product_image_path


class CategoryModel(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to=product_image_path)
    additional_images = models.ManyToManyField(
        "ProductImageModel",
        related_name="additional_images",
        blank=True,
    )
    categories = models.ManyToManyField("CategoryModel", blank=True)

    def __str__(self):
        return f"{self.name} | {self.price}"


class ProductPropertiesModel(models.Model):
    product = models.OneToOneField(
        "ProductModel",
        on_delete=models.CASCADE,
        related_name="properties",
    )
    length = models.FloatField()
    width = models.FloatField()
    high = models.FloatField()
    weight = models.FloatField()


class ProductImageModel(models.Model):
    product = models.ForeignKey(
        "ProductModel", on_delete=models.CASCADE, related_name="product_images"
    )
    image = models.ImageField(upload_to=product_image_path)

    def __str__(self):
        return f"Product: {self.product.id} - Image"
