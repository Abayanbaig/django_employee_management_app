# Generated by Django 2.2 on 2022-04-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0020_auto_20220421_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='vote_ratio',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='vote_total',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
