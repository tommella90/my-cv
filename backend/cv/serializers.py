from rest_framework import serializers
from .models import Education, Experience, ExperienceDescription, EducationDescription

class EducationDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDescription
        fields = ['description']

class EducationSerializer(serializers.ModelSerializer):
    descriptions = EducationDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = ['id', 'title', 'institution', 'location', 'grade', 'start_date', 'end_date', 'ranking', 'descriptions']

class ExperienceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = ['description']

class ExperienceSerializer(serializers.ModelSerializer):
    descriptions = ExperienceDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ['id', 'title', 'company', 'location', 'start_date', 'end_date', 'ranking', 'descriptions']
