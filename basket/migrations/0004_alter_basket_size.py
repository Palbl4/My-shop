# Generated by Django 4.1 on 2022-09-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_alter_basket_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Размер'),
        ),
    ]
