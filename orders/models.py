from django.db import models
from config import settings


class OrderItem(models.Model):
    PROCESSED = 'PR'
    DELIVERED = 'DLV'
    COMPLITED = 'COM'
    ORDER_STATUS_CHOICES = (
        (PROCESSED, 'Заказ в обработке'),
        (DELIVERED, 'Заказ в пути'),
        (COMPLITED, 'Заказ завершен')
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None,
        blank=True, null=True)
    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=ORDER_STATUS_CHOICES,
        default=PROCESSED)
    created = models.DateTimeField(verbose_name='создан',
                                   auto_now_add=True)
    region = models.CharField(max_length=150, verbose_name='Регион')
    city = models.CharField(max_length=150, verbose_name='Город', default='')
    outside = models.CharField(max_length=150, verbose_name='Улица')
    house = models.IntegerField(verbose_name='Дом')
    apartment = models.IntegerField(verbose_name='Квартира', default='')
    phone_number = models.CharField(max_length=16, verbose_name='Телефон',
                                    default='')
    product = models.TextField(verbose_name='Товар')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Продукт - {self.product}'