# Generated by Django 4.1.1 on 2023-05-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderapp", "0012_alter_order_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="orderdetails",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
