# Generated by Django 5.1.3 on 2024-12-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quran", "0008_plan_alter_customuser_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangedetail",
            name="accusername",
            field=models.CharField(default="", max_length=100),
        ),
    ]
