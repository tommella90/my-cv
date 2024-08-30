from django.contrib import admin
from django.urls import path, include
from cv.plot_view import generate_plot
# from .views import send_email_view, run_celery_debug_task

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cv.urls")),  
    path('plot/', generate_plot, name='plot_view'),
    # path('email/', send_email_view, name='send_email'),
    # path('run-task/', run_celery_debugtask, name='run_task'),
]
