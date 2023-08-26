from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/',include('users.urls')),
    path('products/',include('products.urls')),
    path('orders/',include('orders.urls')),
]
