# Generated by Django 5.2 on 2025-04-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekers', '0002_jobseeker_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='skills',
            field=models.JSONField(default=list),
        ),
    ]
