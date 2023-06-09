# Generated by Django 4.1.1 on 2023-04-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="size",
        ),
        migrations.AddField(
            model_name="product",
            name="cover_photo",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AddField(
            model_name="product",
            name="height",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="product",
            name="width",
            field=models.IntegerField(default=1),
        ),
    ]
