# Generated by Django 4.2.5 on 2023-11-19 11:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("offers", "0008_propertyamenity_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="advertisement",
            name="property_coords",
        ),
    ]