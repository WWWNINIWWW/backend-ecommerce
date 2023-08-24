from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    def get_object(self):
        user_id = self.kwargs['user_id']
        product = get_object_or_404(Products,user_id=user_id)
        return product