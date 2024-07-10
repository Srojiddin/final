from django import forms
from apps.appointments.models import Appointment
from django.core.exceptions import ValidationError


class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['fullname', 'choosing_a_doctor', 'date_of_reservation']


# class AppointmentCreateForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['fullname',  'choosing_a_disease', 'choosing_a_doctor','date_of_reservation']

#     def clean(self):
#         cleaned_data = super().clean()
#         date_of_reservation = cleaned_data.get('date_of_reservation')

#         if date_of_reservation:
#             if Appointment.objects.filter(date_of_reservation=date_of_reservation).exists():
#                 raise ValidationError('Запись на прием для данной даты уже существует.')

        # return cleaned_data
    

class AppointmentDetailForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDeleteForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'




