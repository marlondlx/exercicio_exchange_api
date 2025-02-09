from django.urls import path
from .views import get_currencies  # Importando corretamente a função

urlpatterns = [
    path('currencies/', get_currencies, name='get_currencies'),  # Corrigindo a referência para a view
]
