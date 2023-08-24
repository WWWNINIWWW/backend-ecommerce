from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404

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