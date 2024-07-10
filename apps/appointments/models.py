from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.doctors.models import Doctor
from apps.categories.models import Category
from apps.doctors.models import Doctor
from django.conf import settings

from django.core.exceptions import ValidationError



class Appointment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    fullname = models.CharField(max_length=100, verbose_name='ФИО')
    choosing_a_doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name='Выбор врача'
    )
    date_of_reservation = models.DateField(verbose_name='Дата записи')

    def clean(self):
        # Проверяем, есть ли уже запись на прием для данного пользователя на эту дату
        if Appointment.objects.filter( date_of_reservation=self.date_of_reservation).exists():
            raise ValidationError('Запись на прием для данного пользователя на эту дату уже существует.')

    def save(self, *args, **kwargs):
        self.clean()  # Вызываем clean() для выполнения пользовательской валидации
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Запись на прием у {self.fullname}"


class Contact(models.Model):
    ...


# class 