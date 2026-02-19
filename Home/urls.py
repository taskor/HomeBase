from django.urls import path

from . import views

urlpatterns = [
    path("", views.base, name=""),
    path('pomodoro', views.pomodoro, name='pomodoro'),
    path('workout', views.workout, name='workout'),

    # Agendas
    path('agenda', views.agendas, name='agendas'),
    path('monday', views.agendas, name='monday'),
    path('tuesday', views.agendas, name='tuesday'),
    path('wednesday', views.agendas, name='wednesday'),
    path('thursday', views.agendas, name='thursday'),
    path('friday', views.agendas, name='friday'),
    path('saturday', views.agendas, name='saturday'),
    path('sunday', views.agendas, name='sunday'),
    
    
   
]


'''
    
    '''