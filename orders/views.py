from orders.models import Order, Feedback, FeedbackImage
from orders.serializers import OrderSerializer, FeedbackSerializer
from rest_framework import generics,status
from django.shortcuts import get_object_or_404
from users.models import User
from products.models import Products
from django.utils import timezone
from datetime import timedelta,datetime
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from orders.permissions import *

class OrdersList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_Order]
    def create(self, request, *args, **kwargs):
        seller_id = self.request.data.get('seller_id')
        consumer_id = self.request.data.get('consumer_id')
        product_id = self.request.data.get('product_id')
        quantity_buy = self.request.data.get('quantity_buy')
        generics.get_object_or_404(User, id=seller_id)
        generics.get_object_or_404(User, id=consumer_id)
        generics.get_object_or_404(Products, product_id=product_id)
        product = Products.objects.get(product_id=product_id)
        if product.quantity < int(quantity_buy) or product.quantity <=0:
            return Response({"error": "Insufficient quantity available for purchase."}, status=status.HTTP_401_UNAUTHORIZED)
        order_data = {field: value for field, value in self.request.data.items() if field != 'seller_id' and field != 'consumer_id' and field != 'product_id' and field != 'price_total'}
        price_fate, deadline = Freight(product.zip_code_origin, order_data['zip_code_fate'],product.weight,product.length,product.height,product.width)
        deadline = datetime.date(timezone.now())+timedelta(int(deadline))
        price_total = product.price + price_fate
        order = Order.objects.create(seller_id=seller_id,consumer_id=consumer_id,product_id=product_id,price_total=price_total,price_fate=price_fate,deadline=deadline, **order_data)
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_OrderDetail]
    def get_object(self):
        order_id = self.kwargs['order_id']
        order = get_object_or_404(Order,order_id=order_id)
        return order
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.tracking_code != "" and not instance.concluded:
            import requests
            headers,payload = {},{}
            codigo = instance.tracking_code
            url = f"https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo={codigo}"
            cond = True
            while(cond):
                response = requests.request("GET", url, headers=headers, data = payload)
                if response.status_code == 200:
                    json = response.json()
                    if 'eventos' in json and len(json['eventos']) > 0:
                        primeiro_evento = json['eventos'][0]
                        primeiro_status = primeiro_evento['status']
                        cond = False
                        if str(primeiro_status) == 'Objeto entregue ao destinatário':
                            instance.concluded = True
                            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class FeedbacksList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_Feedback]
    
class FeedbacksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsOwner_FeedbackDetail]
    
    def get_object(self):
        feedback_id = self.kwargs['feedback_id']
        feedback = get_object_or_404(Feedback,feedback_id=feedback_id)
        return feedback
    
def Freight(Zip_code_origin,Zip_code_destination,Weight,Length,Height,Width):
    from requests import post
    import xml.etree.ElementTree as ET
    from decimal import Decimal
    data = {
        'nCdEmpresa': '',
        'sDsSenha': '',
        'nCdServico': '41106', #41106 PAC & 40010 SEDEX
        'sCepOrigem': Zip_code_origin,
        'sCepDestino': Zip_code_destination,
        'nVlPeso': Weight,
        'nCdFormato': '1',
        'nVlComprimento': Length,
        'nVlAltura': Height,
        'nVlLargura': Width,
        'nVlDiametro': '0',
        'sCdMaoPropria': 'n',
        'nVlValorDeclarado': '0',
        'sCdAvisoRecebimento': 'n',
    }
    response = post('http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo',data=data)
    if response.status_code == 200:
        price_fate = ET.fromstring(response.content).find(".//{http://tempuri.org/}Valor").text
        deadline = ET.fromstring(response.content).find(".//{http://tempuri.org/}PrazoEntrega").text
        price_fate = Decimal(float(price_fate.replace(',','.')))
        return price_fate,deadline
        
    else:
        print("Erro na solicitação:", response.status_code)
        print(response.content)

@receiver(post_save, sender=Order)
def after_save_order(sender, instance, created, **kwargs):
    if not created:
        if instance.tracking_code != "" and instance.concluded == False:
            import requests
            headers,payload = {},{}
            codigo = instance.tracking_code
            url = f"https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo={codigo}"
            cond = True
            while(cond):
                response = requests.request("GET", url, headers=headers, data = payload)
                if response.status_code == 200:
                    json = response.json()
                    if 'eventos' in json and len(json['eventos']) > 0:
                        primeiro_evento = json['eventos'][0]
                        primeiro_status = primeiro_evento['status']
                        cond = False
                        if str(primeiro_status) == 'Objeto entregue ao destinatário':
                            instance.concluded = True
                            instance.save()
                            return instance
    if instance.posted:
        product = Products.objects.get(product_id=instance.product_id)
        product.quantity-=1
        product.save()
        return product

@receiver(pre_delete, sender=Feedback)
def before_delete_user(sender, instance, **kwargs):
    try:
        feedback_images = FeedbackImage.objects.filter(feedback=instance)
        for image in feedback_images:
            image.image.delete(save=False)
            image.delete()  
    except:
        pass