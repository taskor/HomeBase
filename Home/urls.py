from django.urls import path

from . import views

urlpatterns = [
    path("", views.base, name=""),
    path('pomodoro', views.pomodoro, name='pomodoro'),
    path('workout', views.workout, name='workout'),

    # Agendas
    path('monday', views.agenda, name='monday'),
    path('tuesday', views.agenda, name='tuesday'),
    path('wednesday', views.agenda, name='wednesday'),
    path('thursday', views.agenda, name='thursday'),
    path('friday', views.agenda, name='friday'),
    path('saturday', views.agenda, name='saturday'),
    path('sunday', views.agenda, name='sunday'),
   
]
