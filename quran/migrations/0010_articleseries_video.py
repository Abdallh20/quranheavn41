# Generated by Django 5.1.3 on 2024-12-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quran", "0009_article_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="articleseries",
            name="video",
            field=models.FileField(blank=True, null=True, upload_to="videos/"),
        ),
    ]