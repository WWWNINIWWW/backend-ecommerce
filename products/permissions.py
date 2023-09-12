from rest_framework import permissions
from rest_framework.authtoken.models import Token
from products.models import Products

class IsOwner_ProductDetail(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.auth:
            token = request.auth
            user_id = Token.objects.get(key=token).user.id
            products = Products.objects.filter(user_id=user_id)
            for product in products:
                if token and view.kwargs.get('product_id') == product.product_id:
                    return True
        return False
    
class isOwner_Product(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.auth:
            token = request.auth
            user_id_token = Token.objects.get(key=token).user.id
            user_id_request = int(request.data.get('user_id'))
            if token and user_id_request == user_id_token:
                return True
        return False