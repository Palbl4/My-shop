# Generated by Django 4.1 on 2022-08-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_listofproduct_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizerange',
            name='size_range',
        ),
        migrations.AddField(
            model_name='sizerange',
            name='size',
            field=models.ManyToManyField(to='mainapp.listofproduct'),
        ),
        migrations.RemoveField(
            model_name='listofproduct',
            name='size_range',
        ),
        migrations.AddField(
            model_name='listofproduct',
            name='size_range',
            field=models.IntegerField(null=True),
        ),
    ]
