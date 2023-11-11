# Generated by Django 4.2.5 on 2023-11-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("offers", "0002_alter_advertisement_property_rental_condition_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advertisement",
            name="job_duration",
            field=models.CharField(
                blank=True,
                choices=[
                    ("one_time_task", "Разовое задание"),
                    ("temporary", "Временная работа"),
                    ("permanent", "Постоянная работа"),
                    ("other", "Другое"),
                ],
                max_length=25,
                null=True,
                verbose_name="Продолжительность работы",
            ),
        ),
        migrations.AlterField(
            model_name="advertisement",
            name="transport_body_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("sedan", "Седан"),
                    ("liftback", "Лифтбэк"),
                    ("coupe", "Купе"),
                    ("convertible", "Кабриолет"),
                    ("hatchback", "Хэтчбэк"),
                    ("suv", "Внедорожник"),
                    ("limousine", "Лимузин"),
                    ("pickup", "Пикап"),
                ],
                max_length=50,
                null=True,
                verbose_name="Тип кузова",
            ),
        ),
    ]
