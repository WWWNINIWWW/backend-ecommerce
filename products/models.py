from django.db import models

class Products(models.Model):
    name_product = models.CharField(max_length=255)
    user_id = models.IntegerField(unique=True,null=False)
    product_id = models.IntegerField(unique=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    sale = models.DecimalField(default=0.00, decimal_places=2,max_digits=4)
    quantity = models.IntegerField(default=0,null=False)
    description = models.TextField(default="", null=False)
    assessment = models.TextField(default="", null=False)
    specifications = models.TextField(default="", null=False)
    zip_code_origin = models.IntegerField(default=0,null=False)