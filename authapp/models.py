from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )
    user = models.OneToOneField(ShopUser, unique=True, null=False,
                                db_index=True, on_delete=models.CASCADE)
    gender = models.CharField(
        verbose_name='пол', max_length=1, choices=GENDER_CHOICES,
        blank=True)


@receiver(post_save, sender=ShopUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShopUserProfile.objects.create(user=instance)


@receiver(post_save, sender=ShopUser)
def save_user_profile(sender, instance, **kwargs):
    instance.shopuserprofile.save()
