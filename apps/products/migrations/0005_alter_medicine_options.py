# Generated by Django 5.0.6 on 2024-07-10 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_medicine_image_for_medicine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'Медикамент', 'verbose_name_plural': 'Медикаменты'},
        ),
    ]
