# Generated by Django 5.1.3 on 2024-12-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quran", "0012_alter_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
