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

def agenda(request):
    day_name = timezone.now().strftime("%A")

    MondayDate = datetime(2026, 2, 16)
    MondayWeekday = MondayDate.strftime("%A")
    if day_name == MondayWeekday:
        MondayAgenda = Monday.objects.all
        return render(request, 'Home/agendas/monday.html', {
            MondayAgenda: 'MondayAgenda'
        })

    TuesdayDate = datetime(2026, 2, 17)
    TuesdayWeekday = TuesdayDate.strftime("%A")
    if day_name == TuesdayWeekday:
        TuesdayAgenda = Monday.objects.all
        return render(request, 'Home/agendas/tuesday.html', {
            TuesdayAgenda: 'TuesdayAgenda'
        })

    WednesdayDate = datetime(2026, 2, 18)
    WednesdayWeekday = WednesdayDate.strftime("%A")
    if day_name == WednesdayWeekday:
        WednesdayAgenda = Wednesday.objects.all
        return render(request, 'Home/agendas/wednesday.html', {
            WednesdayAgenda: 'WednesdayAgenda'
        })

    ThursdayDate = datetime(2026, 2, 19)
    ThursdayWeekday = ThursdayDate.strftime("%A")
    if day_name == ThursdayWeekday:
        ThursdayAgenda = Thursday.objects.all
        return render(request, 'Home/agendas/thursday.html', {
            ThursdayAgenda: 'ThursdayAgenda'
        })

    FridayDate = datetime(2026, 2, 20)
    FridayWeekday = FridayDate.strftime("%A")
    if day_name == FridayWeekday:
        FridayAgenda = Friday.objects.all
        return render(request, 'Home/agendas/friday.html', {
            FridayAgenda: 'FridayAgenda'
        })
    
    SaturdayDate = datetime(2026, 2, 21)
    SaturdayWeekday= SaturdayDate.strftime("%A")
    if day_name == SaturdayWeekday:
        SaturdayAgenda = Saturday.objects.all
        return render(request, 'Home/agendas/saturday.html', {
            SaturdayAgenda: 'SaturdayAgenda'
        })
    
    SundayDate = datetime(2026, 2, 22)
    SundayWeekday = SundayDate.strftime("%A")
    if day_name == SundayWeekday:
        SundayAgenda = Monday.objects.all
        return render(request, 'Home/agendas/sunday.html', {
            SundayAgenda: 'SundayAgenda'
        })