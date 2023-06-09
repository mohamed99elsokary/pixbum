# Generated by Django 4.1.1 on 2023-05-27 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0004_user_is_generated_alter_user_is_active"),
        ("orderapp", "0011_order_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="userapp.address",
            ),
        ),
    ]
