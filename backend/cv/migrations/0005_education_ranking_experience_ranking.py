# Generated by Django 5.0.4 on 2024-07-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0004_alter_education_grade"),
    ]

    operations = [
        migrations.AddField(
            model_name="education",
            name="ranking",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="experience",
            name="ranking",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
