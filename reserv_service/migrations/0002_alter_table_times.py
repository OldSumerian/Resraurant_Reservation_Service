# Generated by Django 5.1.1 on 2024-10-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='times',
            field=models.ManyToManyField(blank=True, null=True, to='reserv_service.timesection'),
        ),
    ]
