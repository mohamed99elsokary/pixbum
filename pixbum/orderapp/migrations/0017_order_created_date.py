# Generated by Django 4.1.1 on 2023-06-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orderapp", "0016_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="created_date",
            field=models.DateField(auto_now=True),
        ),
    ]
