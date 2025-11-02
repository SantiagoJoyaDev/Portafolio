from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta principal (página de inicio)
    path('sobre-mi/', views.sobre_mi, name='sobre_mi')
]

