# Generated by Django 4.1.5 on 2024-05-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="user",
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
                ("name", models.CharField(max_length=70)),
                ("email", models.EmailField(max_length=100)),
                ("pasword", models.CharField(max_length=100)),
            ],
        ),
    ]
