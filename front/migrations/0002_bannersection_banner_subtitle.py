# Generated by Django 4.2.14 on 2024-08-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannersection',
            name='banner_subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
