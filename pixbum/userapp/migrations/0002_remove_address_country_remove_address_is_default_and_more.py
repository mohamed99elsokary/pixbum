# Generated by Django 4.1.1 on 2023-04-22 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="country",
        ),
        migrations.RemoveField(
            model_name="address",
            name="is_default",
        ),
        migrations.RemoveField(
            model_name="address",
            name="postal_code",
        ),
        migrations.RemoveField(
            model_name="address",
            name="region",
        ),
    ]
