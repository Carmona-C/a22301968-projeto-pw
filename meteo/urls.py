# meteo/urls.py
from django.urls import path
from .views import previsao_lisboa
from .views import previsao_tempo

app_name = 'meteo'

urlpatterns = [
    path('previsao_lisboa/', previsao_lisboa, name='previsao_lisboa'),
    path('previsao_tempo/', previsao_tempo, name='previsao_tempo'),
]
