from orders.models import Order, Feedback, FeedbackImage
from rest_framework import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from products.models import Products
from users.models import User
from rest_framework.exceptions import ValidationError

class OrderSerializer(serializers.ModelSerializer):
    price_fate = serializers.ReadOnlyField()
    price_total = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    deadline = serializers.ReadOnlyField()
    concluded = serializers.ReadOnlyField()
    seller_id = serializers.ReadOnlyField()
    consumer_id = serializers.ReadOnlyField()
    product_id = serializers.ReadOnlyField()
    
    class Meta:
        model = Order
        fields = ['order_id','seller_id','consumer_id','product_id','zip_code_fate','price_fate','price_total','quantity_buy','deadline','posted','tracking_code','concluded','created_at','modified_at']
     
class FeedbackImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackImage
        fields = ['image']
        
class FeedbackSerializer(serializers.ModelSerializer):
    images = FeedbackImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False)
    class Meta:
        model = Feedback
        fields = ['feedback_id','consumer_id','product_id','assessment','comentary','images','uploaded_images']
    
    def create(self, validaded_data):
        product_id = self.initial_data.get('product_id')
        consumer_id = self.initial_data.get('consumer_id')
        generics.get_object_or_404(Products,product_id=product_id)
        generics.get_object_or_404(User,user_id=consumer_id)
        feedbacks_product = Feedback.objects.filter(product_id=product_id,consumer_id=consumer_id)
        if feedbacks_product.first() != None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        assessment = int(self.initial_data.get('assessment'))
        if assessment >=0 and assessment <=5:
            if self.initial_data.get('uploaded_images'):
                uploaded_images = validaded_data.pop("uploaded_images")
            feedback = Feedback.objects.create(**validaded_data)
            try:
                for image in uploaded_images:
                    newproduct_image = FeedbackImage.objects.create(feedback=feedback,image=image)
            except:
                pass
            return feedback
        raise ValidationError({'error': 'avaliação não permitida.'})
        