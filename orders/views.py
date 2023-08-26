from orders.models import Order, Feedback
from orders.serializers import OrderSerializer, FeedbackSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from users.models import User
from products.models import Products

class OrdersList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def perform_create(self,serializer):
        seller_id = self.request.data.get('seller_id')
        consumer_id = self.request.data.get('consumer_id')
        product_id = self.request.data.get('product_id')
        generics.get_object_or_404(User, user_id=seller_id)
        generics.get_object_or_404(User, user_id=consumer_id)
        generics.get_object_or_404(Products, product_id=product_id)
        order_data = {field: value for field, value in self.request.data.items() if field != 'seller_id' and field != 'consumer_id' and field != 'product_id'}
        order = Order.objects.create(seller_id=seller_id,consumer_id=consumer_id,product_id=product_id, **order_data)
        return order

class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get_object(self):
        order_id = self.kwargs['order_id']
        order = get_object_or_404(Order,order_id=order_id)
        return order
    
class FeedbacksList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
class FeedbacksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer