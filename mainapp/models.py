from django.db import models


class Sex(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS, default='')

    def __str__(self):
        return self.gender


class SizeRange(models.Model):
    size_range = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.size_range)


class ListOfProduct(models.Model):
    title = models.TextField(verbose_name='заголовок')
    preview = models.CharField(max_length=230, verbose_name='Краткое описание',
                               default='', blank=True)
    description = models.TextField(verbose_name='описание', null=True,
                                   blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)
    img = models.TextField(verbose_name='Путь до фото', null=True, blank=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, null=True,
                            blank=True)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2,
                                blank=True)
    size_range = models.ManyToManyField(SizeRange, blank=True)


    def get_size_range(self):
        # return ",".join([str(p) for p in self.size_range.all()])
        return self.size_range.all()

    def __str__(self):
        return f'Модель: {self.title}, Пол:  {self.sex},' \
               f' Размеры: {self.get_size_range()}'

    @staticmethod
    def get_items(user):
        return user.basket.select_related().order_by(
            'product__title')