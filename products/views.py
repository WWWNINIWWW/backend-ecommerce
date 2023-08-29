from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from orders.models import Order

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    def perform_create(self,serializer):
        user_id = self.request.data.get('user_id')
        generics.get_object_or_404(User, user_id=user_id)
        product_data = {field: value for field, value in self.request.data.items() if field != 'user_id'}
        product = Products.objects.create(user_id=user_id, **product_data)
        return product
        
        

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    def get_object(self):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Products,product_id=product_id)
        return product

@receiver(pre_delete, sender=Products)
def before_delete_user(sender, instance, **kwargs):
    try:
        product_id = instance.product_id
        orders = Order.objects.all()
        for order in orders:
            if order.product_id == product_id:
                order.delete()
        return order
    except:
        pass