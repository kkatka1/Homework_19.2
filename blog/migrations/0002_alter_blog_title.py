# Generated by Django 5.1.1 on 2024-10-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=150, verbose_name="заголовок"),
        ),
    ]
