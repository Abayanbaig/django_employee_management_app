# Generated by Django 4.0.4 on 2022-04-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0015_alter_project_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(default='profiles/user-default.png', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
