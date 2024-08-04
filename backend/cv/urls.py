from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationViewSet, ExperienceViewSet

router = DefaultRouter()
router.register(r"education", EducationViewSet)
router.register(r"experience", ExperienceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]