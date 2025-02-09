from django.http import JsonResponse
from datetime import datetime
from .models import CurrencyRate  # Certifique-se de ter esse modelo

def get_currencies(request):
    current_hour = datetime.now().hour
    
    # Exemplo: impedir que a API funcione em horários não comerciais
    if current_hour < 9 or current_hour > 18:
        return JsonResponse({"error": "Consulta permitida apenas entre 09:00 e 18:00"}, status=403)

    currencies = CurrencyRate.objects.all()
    data = {
        "currencies": [
            {"code": currency.code, "name": currency.name, "rate": currency.rate}
            for currency in currencies
        ]
    }
    return JsonResponse(data)
