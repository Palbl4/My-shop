from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from basket.models import Basket
from orders.forms import OrderItemForm
from orders.models import OrderItem


class OrderList(ListView):
    model = OrderItem

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user)


class OrderItemsCreate(CreateView):
    form_class = OrderItemForm
    model = OrderItem
    success_url = reverse_lazy('order:orders_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        product = Basket.objects.filter(user=self.request.user).values()
        form.instance.product = list(product)

        return super().form_valid(form)
