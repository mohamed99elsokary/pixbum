# Generated by Django 4.1.1 on 2023-04-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderapp", "0004_alter_orderdetails_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="is_checkout",
            field=models.BooleanField(default=False),
        ),
    ]
