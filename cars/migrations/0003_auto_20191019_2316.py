# Generated by Django 2.1.5 on 2019-10-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
