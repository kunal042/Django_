# Generated by Django 4.1.5 on 2024-06-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enroll", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("empnum", models.IntegerField(unique=True)),
                ("city", models.CharField(max_length=70)),
                ("salary", models.IntegerField()),
                ("join_date", models.DateField()),
            ],
        ),
    ]
