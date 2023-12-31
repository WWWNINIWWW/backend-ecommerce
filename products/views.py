from products.models import Products,ProImage
from products.serializers import ProductsSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from orders.models import Order,Feedback
from django.db.models import Sum
from decimal import Decimal, ROUND_HALF_UP
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from products.permissions import IsOwner_ProductDetail, isOwner_Product

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [isOwner_Product]

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_ProductDetail]
    def get_object(self):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Products,product_id=product_id)
        feedback = Feedback.objects.filter(product_id=product_id)
        qtd,total = feedback.count(),feedback.aggregate(total_assessment=Sum('assessment'))['total_assessment']
        if total is not None:
            average_assessment = total/qtd
            product.assessment = average_assessment.quantize(Decimal('0.0'), rounding=ROUND_HALF_UP)
            product.save()
        return product

@receiver(pre_delete, sender=Products)
def before_delete_user(sender, instance, **kwargs):
    try:
        product_images = ProImage.objects.filter(product=instance)
        for image in product_images:
            image.image.delete(save=False)
            image.delete()
        orders = Order.objects.filter(product_id=instance.product_id)
        for order in orders:
            order.delete()
        
    except:
        pass