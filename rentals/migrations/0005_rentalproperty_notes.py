# Generated by Django 5.0.10 on 2025-03-22 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rentals", "0004_rentalproperty_monthly_rent"),
    ]

    operations = [
        migrations.AddField(
            model_name="rentalproperty",
            name="notes",
            field=models.TextField(default=""),
        ),
    ]
