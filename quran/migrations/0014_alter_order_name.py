# Generated by Django 5.1.3 on 2024-12-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quran", "0013_alter_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
    ]
