from django.db import models

class Order(models.Model):
    seller_id = models.IntegerField(unique=True,null=False)
    consumer_id = models.IntegerField(unique=True,null=False)
    product_id = models.IntegerField(unique=True,null=False)
    zip_code_fate = models.IntegerField(default=0,null=False)
    price_fate = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    price_total = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    quantity_buy = models.IntegerField(default=0,null=False)

class Feedback(models.Model):
    consumer_id = models.IntegerField(unique=True,null=False)
    product_id = models.IntegerField(unique=True,null=False)
    assessment = models.IntegerField(default=0,null=False)
    comentary = models.TextField(default="", null=False)
