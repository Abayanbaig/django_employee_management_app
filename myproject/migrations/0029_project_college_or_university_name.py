# Generated by Django 4.0.4 on 2022-04-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0028_remove_project_description_project_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='college_or_university_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]