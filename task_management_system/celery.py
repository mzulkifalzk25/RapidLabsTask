from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NIMARFTS.settings')
app = Celery('NIMARFTS')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Karachi')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete_completed_tasks': {
        'task': 'app.tasks.delete_completed_tasks',
        'schedule': crontab(hour=0, minute=0),
    }
}
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')