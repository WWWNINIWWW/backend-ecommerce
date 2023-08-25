from products.models import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['user_id','product_id','name_product','zip_code_origin','price','sale','quantity','assessment','description','specifications','created_at','modified_at']