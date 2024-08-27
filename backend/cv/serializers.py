from rest_framework import serializers
from .models import Education, Experience, ExperienceDescription, EducationDescription, EducationImage, ExperienceImage

class EducationDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDescription
        fields = ['description']


class EducationImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        education_id = self.context.get('education_id')
        if not education_id:
            raise KeyError("Parameter 'education_id' is missing from the context.")
        return EducationImage.objects.create(education_id=education_id, **validated_data)

    class Meta:
        model = EducationImage
        fields = ['id', 'image']


class EducationSerializer(serializers.ModelSerializer):
    images = EducationImageSerializer(many=True, read_only=True)
    descriptions = EducationDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = ['id', 'title', 'institution', 'location', 'grade', 'start_date', 'end_date', 'ranking', 'descriptions', 'images']


class ExperienceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceDescription
        fields = ['description']


class ExperienceImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        experience_id = self.context.get('experience_id')
        if not experience_id:
            raise KeyError("Parameter 'experience_id' is missing from the context.")
        return ExperienceImage.objects.create(experience_id=experience_id, **validated_data)

    class Meta:
        model = ExperienceImage
        fields = ['id', 'image']


class ExperienceSerializer(serializers.ModelSerializer):
    images = ExperienceImageSerializer(many=True, read_only=True)
    descriptions = ExperienceDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ['id', 'title', 'company', 'location', 'start_date', 'end_date', 'ranking', 'descriptions', 'images']


