# Generated by Django 4.0.4 on 2022-04-24 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0031_project_specialization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='specialization',
            new_name='ug_specialization',
        ),
    ]