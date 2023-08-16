from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotelApi.settings')

app = Celery('hotelApi')
app.config_from_object('hotelApi.celeryconfig')

app.conf.update(
    result_expires=3600,
)

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'Delete expired tokens from black list': {
        'task': 'account.tasks.clear_tokens',
        'schedule': crontab(hour='13', minute='28')
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')