from django.db import models

class Order(models.Model):
    order_id = models.IntegerField(unique=True,null=False)
    seller_id = models.IntegerField(null=False)
    consumer_id = models.IntegerField(null=False)
    product_id = models.IntegerField(null=False)
    zip_code_fate = models.IntegerField(default=0,null=False)
    price_fate = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    price_total = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    quantity_buy = models.IntegerField(default=0,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    concluded = models.BooleanField(default=False)
    posted = models.BooleanField(default=False)
    tracking_code = models.TextField(default="")

class Feedback(models.Model):
    feedback_id = models.IntegerField(unique=True)
    consumer_id = models.IntegerField(unique=True,null=False)
    product_id = models.IntegerField(unique=True,null=False)
    assessment = models.IntegerField(default=0,null=False)
    comentary = models.TextField(default="", null=False)
