from django.shortcuts import render
from django.views import generic

from apps.schedules.models import Schedule

from apps.schedules.forms import ScheduleCreateForm


class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'schedules/schedule.html'
    context_object_name = "schedules"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Добавляем форму создания расписания (если используется)
        context['form'] = ScheduleCreateForm()

        # Добавляем данные для каждого дня недели
        context['monday_schedules'] = Schedule.objects.filter(day='Monday')
        context['tuesday_schedules'] = Schedule.objects.filter(day='Tuesday')
        context['wednesday_schedules'] = Schedule.objects.filter(day='Wednesday')
        context['thursday_schedules'] = Schedule.objects.filter(day='Thursday')
        context['friday_schedules'] = Schedule.objects.filter(day='Friday')
        context['saturday_schedules'] = Schedule.objects.filter(day='Saturday')
        context['sunday_schedules'] = Schedule.objects.filter(day='Sunday')

        return context


# class ScheduleView(TemplateView):
#     template_name = 'schedules/schedule.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Фильтрация расписаний по дням недели
#         context['monday_schedules'] = Schedule.objects.filter(day='Monday')
#         context['tuesday_schedules'] = Schedule.objects.filter(day='Tuesday')
#         context['wednesday_schedules'] = Schedule.objects.filter(day='Wednesday')
#         context['thursday_schedules'] = Schedule.objects.filter(day='Thursday')
#         context['friday_schedules'] = Schedule.objects.filter(day='Friday')
#         context['saturday_schedules'] = Schedule.objects.filter(day='Saturday')
#         context['sunday_schedules'] = Schedule.objects.filter(day='Sunday')

#         return context