# Generated by Django 5.0.3 on 2024-04-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecom", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("dept_name", models.CharField(max_length=100)),
                ("dept_desc", models.TextField()),
            ],
        ),
    ]
