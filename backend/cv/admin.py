from django.contrib import admin
from django.utils.html import format_html
from .models import Education, EducationDescription, Experience, ExperienceDescription, EducationImage, ExperienceImage

class EducationDescriptionInline(admin.TabularInline):
    model = EducationDescription

class EducationImageInline(admin.TabularInline):
    model = EducationImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, obj):
        if obj.image and obj.image.name != '':
            return format_html(f'<img src="{obj.image.url}" class="thumbnail" />')
        return "No Image"

    fields = ['image', 'thumbnail']  # Ensure thumbnail is displayed in the form

class ExperienceDescriptionInline(admin.TabularInline):
    model = ExperienceDescription

class ExperienceImageInline(admin.TabularInline):
    model = ExperienceImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, obj):
        if obj.image and obj.image.name != '':
            return format_html(f'<img src="{obj.image.url}" class="thumbnail" />')
        return "No Image"

    fields = ['image', 'thumbnail']  # Ensure thumbnail is displayed in the form

class EducationAdmin(admin.ModelAdmin):
    inlines = [EducationDescriptionInline, EducationImageInline]

    class Media:
        css = {
            'all': ['/static/cv/style.css']  # Ensure the path is correct
        }

class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceDescriptionInline, ExperienceImageInline]

    class Media:
        css = {
            'all': ['/static/cv/style.css']  # Ensure the path is correct
        }

admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
