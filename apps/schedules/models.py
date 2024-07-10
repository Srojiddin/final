
from django.db import models
from apps.doctors.models import Doctor

class Schedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    doctor_name = models.CharField(max_length=100)
    calendar = models.CharField(max_length=100)  # Assuming calendar is a CharField
    choosing_a_doctor = models.ForeignKey(
        'doctors.Doctor',
        on_delete=models.CASCADE,
        verbose_name='Выбор врача'
    )
    level = models.CharField(max_length=100)
    day = models.CharField(max_length=12, choices=DAY_CHOICES)
    experience = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.doctor_name} ({self.calendar})"
