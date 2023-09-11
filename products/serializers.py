from products.models import Products, ProImage
from rest_framework import serializers
from rest_framework import generics
from users.models import User

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProImage
        fields = ['image']

class ProductsSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file=False, use_url=False),
        write_only=True)
    created_at = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    assessment = serializers.ReadOnlyField()
    class Meta:
        model = Products
        fields = ['product_id','user_id','name_product','images','uploaded_images','zip_code_origin','price','sale','quantity','assessment','description','specifications','weight','length','height','width','created_at','modified_at']
    
    def create(self, validaded_data):
        user_id = self.initial_data.get('user_id')
        generics.get_object_or_404(User, id=user_id)
        uploaded_images = validaded_data.pop("uploaded_images")
        product = Products.objects.create(**validaded_data)
        for image in uploaded_images:
            newproduct_image = ProImage.objects.create(product=product,image=image)
        return product