from django.shortcuts import render
from .tasks import send_email_task
from django.http import HttpResponse

def run_celery_debug_task(request):
    send_email_task.delay('hello')
    return HttpResponse("Task has been sent")


def send_email_view(request):
    send_email_task.delay('hello')
    return HttpResponse("Email task has been sent")
