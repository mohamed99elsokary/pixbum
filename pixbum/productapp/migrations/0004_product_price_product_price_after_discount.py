# Generated by Django 4.1.1 on 2023-04-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productapp", "0003_product_main_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="product",
            name="price_after_discount",
            field=models.IntegerField(default=1),
        ),
    ]
