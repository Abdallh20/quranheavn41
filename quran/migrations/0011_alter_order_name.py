# Generated by Django 5.1.3 on 2024-12-21 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quran", "0010_remove_exchangedetail_accusername_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="name",
            field=models.OneToOneField(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]