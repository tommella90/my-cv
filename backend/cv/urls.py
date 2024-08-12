from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import EducationViewSet, ExperienceViewSet
from .plot_view import generate_plot  
from django.contrib import admin

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"education", EducationViewSet)
router.register(r"experience", ExperienceViewSet)

urlpatterns = [
    path("", include(router.urls)),  # Include DRF router URLs
    path('plot/', generate_plot, name='plot_view'), 
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
