from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from products.models import Products
from orders.models import Order

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
        return product,order
    except:
        pass