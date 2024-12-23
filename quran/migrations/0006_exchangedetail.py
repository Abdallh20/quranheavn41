# Generated by Django 5.1.3 on 2024-12-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quran", "0005_fatwa_name_alter_article_article_slug_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExchangeDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_cash_wallet", models.CharField(max_length=20)),
                ("screenshot", models.ImageField(upload_to="screenshots/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
