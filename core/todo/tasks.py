import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from celery import shared_task
from .models import Task


@shared_task
def delete_completed_tasks():
    Task.objects.filter(is_completed=True).delete()
