from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta línea es clave
]
