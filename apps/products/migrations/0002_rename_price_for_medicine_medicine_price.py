# Generated by Django 5.0.6 on 2024-07-09 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='price_for_medicine',
            new_name='price',
        ),
    ]
