from orders.models import Order, Feedback
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    price_fate = serializers.ReadOnlyField()
    price_total = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    modified_at = serializers.ReadOnlyField()
    deadline = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = ['order_id','seller_id','consumer_id','product_id','zip_code_fate','price_fate','price_total','quantity_buy','deadline','created_at','modified_at']
        
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['consumer_id','product_id','assessment','comentary']