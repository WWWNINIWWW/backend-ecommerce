from django.db import models

def custom_upload_to(instance, filename):
    return f'media/feedback/{filename}'

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
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
    feedback_id = models.AutoField(primary_key=True)
    consumer_id = models.IntegerField(null=False)
    product_id = models.IntegerField(null=False)
    assessment = models.DecimalField(default=0.0,decimal_places=1,max_digits=2)
    comentary = models.TextField(default="", null=False)
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, default ='')
    
class FeedbackImage(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)