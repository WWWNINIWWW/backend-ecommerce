from users.models import Cart, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.ReadOnlyField()
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email','image','created_at','modified_at']
        
class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    shoppingcart = serializers.ReadOnlyField()
    class Meta:
        model = Cart
        fields= ['user_id','shoppingcart','modified_at']