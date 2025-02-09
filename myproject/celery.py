# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nome_do_projeto.settings")

app = Celery("nome_do_projeto")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
