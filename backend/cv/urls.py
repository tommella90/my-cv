from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import EducationViewSet, ExperienceViewSet, EducationImageViewSet, ExperienceImageViewSet
from .plot_view import generate_plot  
from django.contrib import admin

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"education", EducationViewSet)
router.register(r"experience", ExperienceViewSet)

router.register(r'education/(?P<education_pk>\d+)/images', EducationImageViewSet, basename='education-images')
router.register(r'experience/(?P<experience_pk>\d+)/images', ExperienceImageViewSet, basename='experience-images')

urlpatterns = [
    path("", include(router.urls)),  
    path('plot/', generate_plot, name='plot_view'), 
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
