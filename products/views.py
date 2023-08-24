from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from users.models import User

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
        user_id = self.kwargs['user_id']
        product = get_object_or_404(Products,user_id=user_id)
        return product