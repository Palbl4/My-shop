from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.OrderList.as_view(), name='orders_list'),
    path('create/', views.OrderItemsCreate.as_view(), name='order_create'),
]
