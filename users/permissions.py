from rest_framework import permissions
from rest_framework.authtoken.models import Token

class IsOwner_User(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.auth:
            token = request.auth  
            user_id = Token.objects.get(key=token).user.id
            if token and request.parser_context['kwargs'].get('id') == user_id:
                return True
        return False
        
class IsOwner_Cart(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.auth:
            token = request.auth  
            user_id = Token.objects.get(key=token).user.id
            if token and request.parser_context['kwargs'].get('user_id') == user_id:
                return True
        return False

class IsOwner_CartADDandRemove(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return False
        if request.auth:
            token = request.auth  
            user_id = Token.objects.get(key=token).user.id
            if token and request.parser_context['kwargs'].get('user_id') == user_id:
                return True    
        return False  
