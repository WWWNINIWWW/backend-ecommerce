from users.models import Cart, User
from rest_framework import serializers

#from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email','created_at','modified_at']

"""class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','name','created_at','modified_at']"""
        
class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    shoppingcart = serializers.ReadOnlyField()
    class Meta:
        model = Cart
        fields= ['user_id','shoppingcart','modified_at']