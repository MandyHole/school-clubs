# Generated by Django 3.2.18 on 2023-04-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0031_auto_20230411_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='confirmation',
            field=models.BooleanField(default=False, verbose_name='I am aware that it costs £2/Breakfast and £2.50/Supper*'),
        ),
    ]
