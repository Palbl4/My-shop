# Generated by Django 4.1 on 2022-09-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_basket_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Размер'),
        ),
    ]