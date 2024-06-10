from django.urls import path
from . import views

app_name = 'festivais'

urlpatterns = [
    path('', views.principal_view, name='principal'),
    path('festival/<int:festival_id>/', views.festival_view, name='festival'),
    path('localizacao/<int:localizacao_id>/', views.localizacao_view, name='localizacao'),
]
