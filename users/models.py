from django.db import models
from django.contrib.auth.models import AbstractUser

def custom_upload_to(instance, filename):
    return f'media/user/{instance.id}-{filename}'

class User(AbstractUser):
    email =  models.EmailField(unique=True,default="example@example")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, default ='media/user/defaultProfile.jpg')
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ["username"]
    
class Cart(models.Model):
    user_id = models.IntegerField(unique=True,null=False)
    shoppingcart = models.JSONField(default=dict)
    modified_at = models.DateTimeField(auto_now=True)