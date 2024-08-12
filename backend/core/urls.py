from django.contrib import admin
from django.urls import path, include
from cv.plot_view import generate_plot

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("cv.urls")),  
    path('plot/', generate_plot, name='plot_view'), 
]

