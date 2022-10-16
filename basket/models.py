from django.db import models
from django.conf import settings
from mainapp.models import ListOfProduct, SizeRange, Sex


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket')
    product = models.ForeignKey(ListOfProduct,
                                on_delete=models.CASCADE)
    add_datetime = models.DateTimeField(verbose_name='время',
                                        auto_now_add=True)
    size = models.CharField(max_length=200, verbose_name='Размер', blank=True,
                            null=True)

    def __str__(self):
        return self.product.title

    @property
    def cost(self):
        return self.product.price * len(self.size.split(','))

    @property
    def total_cost(self):
        product = Basket.objects.filter(user=self.user)
        total_cost = sum(map(lambda x: x.cost, product))
        return total_cost

    @property
    def count_size(self):
        return len(self.size.split(','))

    @staticmethod
    def get_items(user):
        return user.basket.select_related().order_by(
            'product__title')