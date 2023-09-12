from users.models import Cart, User
from users.serializers import UserSerializer, CartSerializer
from rest_framework import generics,status
from django.shortcuts import get_object_or_404
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from products.models import Products
from orders.models import Order
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authtoken.models import Token
from users.permissions import IsOwner_User, IsOwner_Cart, IsOwner_CartADDandRemove

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_User]
    
class UserDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_User]
    def get_object(self):
        user_id = self.kwargs['id']
        user = get_object_or_404(User,id=user_id)
        return user
    
class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    
class CartDetailChangeAndDelete(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_Cart]
    def get_object(self):
        user_id = self.kwargs['user_id']
        cart = get_object_or_404(Cart,user_id=user_id)
        return cart
    
class CartProductAdd(generics.UpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_CartADDandRemove]
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
    
class CartProductRemove(generics.UpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_CartADDandRemove]
    def put(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Products,product_id=product_id)
        cart = get_object_or_404(Cart,user_id=user_id)
        if str(product.product_id) in cart.shoppingcart:
            del cart.shoppingcart[str(product.product_id)]
            cart.save()
            serializer = self.get_serializer(cart)
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return (Response(status=status.HTTP_404_NOT_FOUND))
    
@receiver(pre_delete, sender=User)
def before_delete_user(sender, instance, **kwargs):
    try:
        user_id = instance.id
        products = Products.objects.filter(user_id=user_id)
        orders = Order.objects.all()
        for product in products:
            product.delete()
        for order in orders:
            if order.seller_id == user_id or order.consumer_id == user_id:
                order.delete()
        cart = Cart.objects.filter(user_id=user_id).first().delete()
    except:
        pass

@receiver(post_save, sender=User)
def after_save_user(sender, instance, created, **kwargs):
    if created:
        cart = Cart.objects.create(user_id=instance.id)
        return cart