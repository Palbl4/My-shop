# Generated by Django 4.1 on 2022-08-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_listofproduct_img_alter_sizerange_size_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofproduct',
            name='img',
            field=models.TextField(verbose_name='Путь до фото'),
        ),
    ]