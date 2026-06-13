from celery import Celery

app = Celery(
    "airportsite"
)

app.conf.broker_url = "memory://"
app.conf.result_backend = "cache+memory://"

app.autodiscover_tasks()