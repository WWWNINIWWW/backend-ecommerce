from products.models import Products
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    assessment = serializers.ReadOnlyField()
    class Meta:
        model = Products
        fields = ['product_id','user_id','name_product','zip_code_origin','price','sale','quantity','assessment','description','specifications','weight','length','height','width','created_at','modified_at']