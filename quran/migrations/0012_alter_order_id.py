# Generated by Django 5.1.3 on 2024-12-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quran", "0011_alter_order_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]