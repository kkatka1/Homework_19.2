# Generated by Django 5.1.1 on 2024-10-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Введите цену товара",
                max_digits=10,
                verbose_name="Цена",
            ),
        ),
    ]
