# Generated by Django 5.0.6 on 2024-12-16 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
    ]
