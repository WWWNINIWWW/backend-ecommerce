from users.models import User, Cart
from users.serializers import UserSerializer, CartSerializer
from rest_framework import generics,status
from django.shortcuts import get_object_or_404
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from products.models import Products
from orders.models import Order
from rest_framework.response import Response

class UserListAndCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_object(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User,user_id=user_id)
        return user
    
class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartDetailChangeAndDelete(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def get_object(self):
        user_id = self.kwargs['user_id']
        cart = get_object_or_404(Cart,user_id=user_id)
        return cart
    
class CartProductAdd(generics.UpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class = CartSerializer
    def put(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        product_id = self.kwargs['product_id']
        quantity = int(self.request.data.get('quantity'))
        product = get_object_or_404(Products,product_id=product_id)
        cart = get_object_or_404(Cart,user_id=user_id)
        if quantity > product.quantity:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        cart.shoppingcart[product.product_id] = quantity
        cart.save()
        serializer = self.get_serializer(cart)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
@receiver(pre_delete, sender=User)
def before_delete_user(sender, instance, **kwargs):
    try:
        user_id = instance.user_id
        products = Products.objects.all()
        orders = Order.objects.all()
        for product in products:
            if product.user_id == user_id:
                product.delete()
        for order in orders:
            if order.seller_id == user_id or order.consumer_id == user_id:
                order.delete()
        cart = Cart.objects.filter(user_id=user_id).first().delete()
        return product,order,cart
    except:
        pass

@receiver(post_save, sender=User)
def after_save_user(sender, instance, created, **kwargs):
    if created:
        cart = Cart.objects.create(user_id=instance.user_id)
        return cart