# Generated by Django 5.0.4 on 2024-08-01 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0007_educationdescription"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="education",
            name="description",
        ),
    ]
