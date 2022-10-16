from django.urls import path

import basket.views as basket

app_name = 'basket'

urlpatterns = [
    path('', basket.basket, name='view'),
    path('add/<int:pk>/', basket.basket_add, name='add'),
    path('remove/<int:pk>/', basket.basket_remove, name='remove'),
]
