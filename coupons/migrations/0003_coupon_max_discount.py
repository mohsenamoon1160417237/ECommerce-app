# Generated by Django 2.2 on 2020-08-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20200808_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='max_discount',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
