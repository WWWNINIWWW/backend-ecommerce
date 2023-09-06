from users.models import User, Cart
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','name','created_at','modified_at']
        
class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    shoppingcart = serializers.ReadOnlyField()
    class Meta:
        model = Cart
        fields= ['user_id','shoppingcart','modified_at']