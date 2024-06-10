from django.urls import path
from .views import principal_view
from .views import sobre_mim_view
from .views import web_view

app_name = 'portofolio'

urlpatterns = [
    path('', principal_view, name='principal'),
    path('sobre_mim/', sobre_mim_view, name='sobre_mim'),
    path('web/', web_view, name='web'),


]