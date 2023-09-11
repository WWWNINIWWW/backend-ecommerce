from django.urls import path
from users.views import UserListAndCreate,UserDetailChangeAndDelete, CartList,CartDetailChangeAndDelete, CartProductAdd,CartProductRemove
from django.urls import re_path
from users import views


urlpatterns = [
    path('',UserListAndCreate.as_view()),
    path('<int:id>/',UserDetailChangeAndDelete.as_view()),
    path('cart/', CartList.as_view()),
    path('cart/<int:user_id>/',CartDetailChangeAndDelete.as_view()),
    path('cart/<int:user_id>/qty/<int:product_id>/',CartProductAdd.as_view()),
    path('cart/<int:user_id>/remove/<int:product_id>/',CartProductRemove.as_view()),
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
]
