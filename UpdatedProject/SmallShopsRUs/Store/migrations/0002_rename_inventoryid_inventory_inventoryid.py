# Generated by Django 4.2 on 2023-04-30 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='inventoryId',
            new_name='inventoryID',
        ),
    ]