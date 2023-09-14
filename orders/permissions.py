from rest_framework import permissions
from rest_framework.authtoken.models import Token
from orders.models import Order

class IsOwner_Order(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.auth and request.method == 'POST':
            token = request.auth
            user_id_token = Token.objects.get(key=token).user.id
            consumer_id_request = int(request.data.get('consumer_id'))
            if token and consumer_id_request == user_id_token:  
                return True
        return False

class IsOwner_OrderDetail(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.auth:
            token = request.auth
            user_id = Token.objects.get(key=token).user.id
            orders_seller = Order.objects.filter(seller_id=user_id)
            orders_consumer = Order.objects.filter(consumer_id=user_id)
            for order in orders_seller:
                if token and view.kwargs.get('order_id') == order.order_id:
                    return True
            for order in orders_consumer:
                if token and view.kwargs.get('order_id') == order.order_id:
                    return True
        return False