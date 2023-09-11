from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class User(AbstractUser):
    email =  models.EmailField(unique=True,default="example@example")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ["username"]
    
class Cart(models.Model):
    user_id = models.IntegerField(unique=True,null=False)
    shoppingcart = models.JSONField(default=dict)
    modified_at = models.DateTimeField(auto_now=True)