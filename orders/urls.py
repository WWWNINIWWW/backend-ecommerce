from django.urls import path
from orders.views import OrdersList, OrdersDetail, FeedbacksList, FeedbacksDetail

urlpatterns = [
    path('',OrdersList.as_view()),
    path('<int:order_id>/',OrdersDetail.as_view()),
    path('feedback/',FeedbacksList.as_view()),
    path('feedback/<int:feedback_id>/',FeedbacksDetail.as_view()),
]