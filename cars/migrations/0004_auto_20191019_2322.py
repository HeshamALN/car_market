# Generated by Django 2.1.5 on 2019-10-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20191019_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
