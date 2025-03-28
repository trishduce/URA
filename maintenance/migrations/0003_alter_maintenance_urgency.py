# Generated by Django 5.0.10 on 2025-03-22 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintenance", "0002_maintenance_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="maintenance",
            name="urgency",
            field=models.CharField(
                choices=[("Low", "Low"), ("High", "High")],
                default="Medium",
                max_length=10,
            ),
        ),
    ]
