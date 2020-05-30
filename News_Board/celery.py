from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News_Board.settings')

app = Celery('News_Board')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.CELERYBEAT_SCHEDULE = {
    "delete_table": {
        "task": "news.tasks.clean_upvote",
        "schedule": crontab(hour="*/24"),
    }
}




