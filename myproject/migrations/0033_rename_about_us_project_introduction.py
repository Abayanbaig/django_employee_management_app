# Generated by Django 4.0.4 on 2022-04-24 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0032_rename_specialization_project_ug_specialization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='about_us',
            new_name='introduction',
        ),
    ]
