# Generated by Django 2.1.5 on 2019-10-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
