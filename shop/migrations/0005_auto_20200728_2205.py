# Generated by Django 2.2 on 2020-07-28 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200728_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.Catalog'),
        ),
    ]
