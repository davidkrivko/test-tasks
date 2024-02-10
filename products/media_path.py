import os
from uuid import uuid4


def product_image_path(instance, filename):
    # Generate a unique filename using a UUID
    unique_filename = f"{uuid4().hex}{os.path.splitext(filename)[1]}"

    if hasattr(instance, 'name'):
        name = instance.name.replace(" ", "_")
    else:
        name = instance.product.name.replace(" ", "_")
    # Construct the upload path based on the model and unique filename
    return f"product_images/{name}/{unique_filename}"
