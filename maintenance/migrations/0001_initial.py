# Generated by Django 5.0.10 on 2025-03-21 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rentals", "0003_alter_rentalproperty_apt_number_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Maintenance",
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
                (
                    "urgency",
                    models.CharField(
                        choices=[
                            ("Low", "Low"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                        ],
                        default="Medium",
                        max_length=10,
                    ),
                ),
                ("date_reported", models.DateTimeField(auto_now_add=True)),
                ("pending", models.BooleanField(default=True)),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rentals.rentalproperty",
                    ),
                ),
            ],
        ),
    ]
