# Generated by Django 5.0.6 on 2024-07-06 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_pizzas", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="pizzas",
            table="pizza_mysql",
        ),
    ]
