# Generated by Django 5.0.4 on 2024-08-06 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0008_remove_education_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="education",
            name="subtitle",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="experience",
            name="role",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="experience",
            name="subtitle",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
