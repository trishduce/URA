# Generated by Django 5.0.10 on 2025-03-23 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rentals", "0009_alter_rentalproperty_monthly_rent"),
    ]

    operations = [
        migrations.AddField(
            model_name="rentalproperty",
            name="apt_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
