# Generated by Django 3.0.3 on 2020-04-05 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0002_additionalmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='value',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]