# Generated by Django 2.1.15 on 2023-04-18 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ingridients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingridients',
            new_name='Ingredient',
        ),
    ]
