# Generated by Django 5.0.6 on 2024-07-10 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_alter_schedule_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=12),
        ),
    ]