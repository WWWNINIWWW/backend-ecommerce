from django.urls import path
from users.views import UserListAndCreate,UserDetailChangeAndDelete, CartList,CartDetailChangeAndDelete, CartProductAdd


urlpatterns = [
    path('',UserListAndCreate.as_view()),
    path('<int:user_id>/',UserDetailChangeAndDelete.as_view()),
    path('cart/', CartList.as_view()),
    path('cart/<int:user_id>/',CartDetailChangeAndDelete.as_view()),
    path('cart/<int:user_id>/qty/<int:product_id>/',CartProductAdd.as_view()),
]
