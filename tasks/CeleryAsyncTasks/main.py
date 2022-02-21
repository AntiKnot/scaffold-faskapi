from time import sleep

from celery import Celery

BROKER_URL = 'redis://root:123456@localhost:6379/7'
CELERY_RESULT_BACKEND = 'redis://root:123456@localhost:6379/8'

app = Celery('main', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.task(name='test')
def add(x, y):
    return x + y


@app.task(name='send_mail')
def send_mail(mail):
    return '发送成功'
