from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def health_check(request):
    current_time = datetime.utcnow().isoformat() + "Z"
    response_data = {
        "status": "online",
        "message": "O sistema está funcionando normalmente",
        "timestamp": current_time
    }
    return JsonResponse(response_data)

# Create your views here.
