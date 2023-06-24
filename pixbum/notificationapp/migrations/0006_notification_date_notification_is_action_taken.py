# Generated by Django 4.1.1 on 2022-12-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notificationapp", "0005_notification_is_seen"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="notification",
            name="is_action_taken",
            field=models.BooleanField(default=False),
        ),
    ]