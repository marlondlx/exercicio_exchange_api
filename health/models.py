from django.db import models

# Create your models here.

# exchange/models.py
from django.db import models

class SyncStatus(models.Model):
    last_sync = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default="unknown")
