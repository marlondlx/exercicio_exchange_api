# exchange/tasks.py
from celery import shared_task
import requests
from datetime import datetime
from .models import SyncStatus

@shared_task
def sync_exchange_rates():
    from django.conf import settings
    
    url = f"{settings.EXCHANGE_RATE_API_URL}?apikey={settings.EXCHANGE_RATE_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        SyncStatus.objects.update_or_create(
            id=1,
            defaults={"last_sync": datetime.utcnow(), "status": "success"}
        )
    else:
        SyncStatus.objects.update_or_create(
            id=1,
            defaults={"last_sync": datetime.utcnow(), "status": "failed"}
        )
