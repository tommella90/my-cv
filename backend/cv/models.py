from django.db import models
from .validators import validate_file_size

class Education(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100, default='')
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100)
    grade = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.institution} at {self.title}"


class EducationImage(models.Model):
    education = models.ForeignKey(Education, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='education_images/')


class EducationDescription(models.Model):
    education = models.ForeignKey(Education, related_name="descriptions", on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default='')
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.title} at {self.company}"


class ExperienceDescription(models.Model):
    experience = models.ForeignKey(Experience, related_name="descriptions", on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description


class ExperienceImage(models.Model):
    experience = models.ForeignKey(Experience, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="experience_images/", 
        validators=[validate_file_size]
        )