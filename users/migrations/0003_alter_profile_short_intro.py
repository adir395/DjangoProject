# Generated by Django 5.0.6 on 2024-12-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='short_intro',
            field=models.CharField(blank=True, default='This is a default intro. Please enter your profession here.', max_length=200, null=True),
        ),
    ]