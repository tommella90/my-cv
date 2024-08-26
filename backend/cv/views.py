from django.http import HttpResponse
from django.template import loader
import requests
import plotly.graph_objects as go

# Existing viewsets
from rest_framework import viewsets
from .models import Education, Experience, EducationImage, ExperienceImage
from .serializers import EducationSerializer, ExperienceSerializer, EducationImageSerializer, ExperienceImageSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.prefetch_related('images').all()
    serializer_class = EducationSerializer

    def get_queryset(self):
        return Education.objects.all().order_by("ranking").reverse()
        

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.prefetch_related('images').all()
    serializer_class = ExperienceSerializer
    
    def get_queryset(self):
        return Experience.objects.all().order_by("ranking").reverse()


class EducationImageViewSet(viewsets.ModelViewSet):
    serializer_class = EducationImageSerializer

    def get_queryset(self):
        education_id = self.kwargs.get('education_pk')
        if not education_id:
            raise KeyError("Parameter 'education_pk' is missing from the URL.")
        return EducationImage.objects.filter(education_id=education_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['education_id'] = self.kwargs.get('education_pk')
        return context


class ExperienceImageViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceImageSerializer

    def get_queryset(self):
        experience_id = self.kwargs.get('experience_pk')
        if not experience_id:
            raise KeyError("Parameter 'experience_pk' is missing from the URL.")
        return ExperienceImage.objects.filter(experience_id=experience_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['experience_id'] = self.kwargs.get('experience_pk')
        print("Serializer Context:", context)  # Debugging line
        return context
