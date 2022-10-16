
from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('mens-shoes', views.mens_shoes, name='men'),
    path('womans-shoes', views.womans_shoes, name='woman'),
    path('product/<int:pk>/', views.product, name='product')
]
