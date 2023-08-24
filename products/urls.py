from django.urls import path
from products.views import ProductsList,ProductsDetail

urlpatterns = [
    path('',ProductsList.as_view()),
    path('<int:user_id>/',ProductsDetail.as_view()),
]