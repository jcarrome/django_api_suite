from django.urls import path
from .views import LandingAPI

urlpatterns = [
    path('index/', LandingAPI.as_view(), name='landing-index'),  # Ruta base para la vista LandingAPI
]
