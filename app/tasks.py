from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from .models import Task

    
@shared_task
def delete_completed_tasks():
    threshold_date = timezone.now() - timedelta(days=2)
    Task.objects.filter(status='completed', due_date__lt=threshold_date).delete()


@shared_task
def test():
    print('Zulkifal here!')
