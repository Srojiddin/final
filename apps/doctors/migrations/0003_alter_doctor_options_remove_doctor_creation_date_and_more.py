# Generated by Django 5.0.6 on 2024-07-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_doctor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={},
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='creation_date',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='choosing_a_specialization',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Gynaecologist', 'Gynaecologist'), ('Neurologist', 'Neurologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Paediatrician', 'Paediatrician'), ('General Practitioner', 'General Practitioner')], max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image_for_doctor',
            field=models.ImageField(upload_to='doctors/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]