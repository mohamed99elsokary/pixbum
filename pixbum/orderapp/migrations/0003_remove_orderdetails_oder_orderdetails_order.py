# Generated by Django 4.1.1 on 2023-04-22 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orderapp", "0002_orderdetails_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderdetails",
            name="oder",
        ),
        migrations.AddField(
            model_name="orderdetails",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="orderapp.order",
            ),
        ),
    ]
