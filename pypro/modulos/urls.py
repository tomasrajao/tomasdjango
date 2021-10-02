from django.urls import path

from pypro.modulos import views
from pypro.modulos.models import Modulo

app_name = 'modulos'
urlpatterns = [
    path('', views.indice, name='indice'),
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path(f'aulas/<slug:slug>', views.aula, name='aula'),
]
