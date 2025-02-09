from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('health.urls')),  # Rota para o app health
    path('api/', include('exchange.urls')),  # Rota para o app exchange
]
