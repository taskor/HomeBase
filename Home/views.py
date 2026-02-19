from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from .models import *

# Create your views here.

def base(request):
    return render(request, "Home/base.html")

def pomodoro(request):
    return render(request, 'Home/pomodoro.html')

def workout(request):
    return render(request, 'Home/workout.html')

def agendas(request):
    MondayDate = datetime(2026, 2, 16)
    MondayWeekday = MondayDate.strftime("%A")
    TuesdayDate = datetime(2026, 2, 17)
    TuesdayWeekday = TuesdayDate.strftime("%A")
    WednesdayDate = datetime(2026, 2, 18)
    WednesdayWeekday = WednesdayDate.strftime("%A")
    ThursdayDate = datetime(2026, 2, 19)
    ThursdayWeekday = ThursdayDate.strftime("%A")
    FridayDate = datetime(2026, 2, 20)
    FridayWeekday = FridayDate.strftime("%A")
    SaturdayDate = datetime(2026, 2, 21)
    SaturdayWeekday= SaturdayDate.strftime("%A")
    SundayDate = datetime(2026, 2, 22)
    SundayWeekday = SundayDate.strftime("%A")
    day_name = timezone.now().strftime("%A")
    return render(request, 'Home/agendas.html', {
        'MondayDate': MondayDate,
        'MondayWeekday': MondayWeekday,
        'TuesdayDate': TuesdayDate,
        'TuesdayWeekday': TuesdayWeekday,
        'WednesdayDate': WednesdayDate,
        'WednesdayWeekday': WednesdayWeekday,
        'ThursdayDate': ThursdayDate,
        'ThursdayWeekday': ThursdayWeekday,
        'FridayDate': FridayDate,
        'FridayWeekday': FridayWeekday,
        'FridayDate': FridayDate,
        'FridayWeekday': FridayWeekday,
        'SaturdayDate': SaturdayDate,
        'SaturdayWeekday': SaturdayWeekday,
        'SundayDate': SundayDate,
        'SundayWeekday': SundayWeekday,
        'DayName': day_name,

    })
   
        