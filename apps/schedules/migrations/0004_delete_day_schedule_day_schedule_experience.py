# Generated by Django 5.0.6 on 2024-07-10 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_day'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[('Wednesday', 'Wednesday'), ('Tuesday', 'Tuesday'), ('Sunday', 'Sunday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Monday', 'Monday'), ('Thursday', 'Thursday')], default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='experience',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]