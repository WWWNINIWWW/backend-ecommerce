from django.db import models

def custom_upload_to(instance, filename):
    return f'media/products/{instance.product.product_id}-{filename}'

class Products(models.Model):
    name_product = models.CharField(max_length=255)
    user_id = models.IntegerField(null=False)
    product_id = models.IntegerField(unique=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    sale = models.DecimalField(default=0.00, decimal_places=2,max_digits=4)
    quantity = models.IntegerField(default=0,null=False)
    description = models.TextField(default="", null=False)
    assessment = models.IntegerField(default=0,null=False)
    specifications = models.TextField(default="", null=False)
    zip_code_origin = models.IntegerField(default=0,null=False)
    weight = models.IntegerField(default=0,null=False)
    length = models.IntegerField(default=0,null=False)
    height = models.IntegerField(default=0,null=False)
    width = models.IntegerField(default=0,null=False)
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, default ='')
    
class ProImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)