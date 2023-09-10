# Generated by Django 4.2.5 on 2023-09-10 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_remove_attributes_product_product_attributes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='attributes',
            options={'verbose_name': 'Аттрибут', 'verbose_name_plural': 'Аттрибуты'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегории'},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.product', verbose_name='Товар'),
        ),
    ]
