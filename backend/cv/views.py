from django.http import HttpResponse
from django.template import loader
import requests
import plotly.graph_objects as go

# Existing viewsets
from rest_framework import viewsets
from .models import Education, Experience
from .serializers import EducationSerializer, ExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get_queryset(self):
        return Education.objects.all().order_by("ranking").reverse()

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    
    def get_queryset(self):
        return Experience.objects.all().order_by("ranking").reverse()
