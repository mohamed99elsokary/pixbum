# Generated by Django 4.1.1 on 2023-07-07 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notificationapp", "0007_notification_is_clicked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_notifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
