from django.contrib import admin
from .models import Education, EducationDescription, Experience, ExperienceDescription

class ExperienceDescriptionInline(admin.TabularInline):
    model = ExperienceDescription
    extra = 2

class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceDescriptionInline]


class EducationDescriptionInline(admin.TabularInline):
    model = EducationDescription
    extra = 2

class EducationAdmin(admin.ModelAdmin):
    inlines = [EducationDescriptionInline]


admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
