# Generated by Django 5.0.6 on 2024-07-10 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_name_medicine_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='image_for_medicine',
            field=models.ImageField(blank=True, null=True, upload_to='medicines/', verbose_name='Изображение'),
        ),
    ]
