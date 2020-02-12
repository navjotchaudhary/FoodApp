# Generated by Django 3.0.2 on 2020-01-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/product/food/images'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/product/restaurant/images'),
        ),
    ]
