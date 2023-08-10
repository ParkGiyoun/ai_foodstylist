# Generated by Django 4.2.4 on 2023-08-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="chat_message",
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
                ("role", models.CharField(max_length=30)),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
