from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health_check, name='health_check'),
]

# urls.py
from django.urls import path
from .views import health_check

urlpatterns = [
    path("health", health_check, name="health"),
]
