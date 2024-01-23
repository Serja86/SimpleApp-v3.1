from celery import shared_task

import time, printer


@shared_task
def hello():
    time.sleep(10)
    print('Hello, world!')