# Generated by Django 4.1.1 on 2023-05-27 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderapp", "0013_order_total_price_orderdetails_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderdetails",
            name="extra",
            field=models.IntegerField(default=0),
        ),
    ]