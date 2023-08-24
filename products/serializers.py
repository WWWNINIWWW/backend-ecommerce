from products.models import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['user_id','name_product','created_at','modified_at']