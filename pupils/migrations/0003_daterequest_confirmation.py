# Generated by Django 3.2.18 on 2023-04-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0002_daterequest_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='daterequest',
            name='confirmation',
            field=models.BooleanField(default=False, verbose_name='I am aware that it costs £2/Breakfast and £2.50/Supper*'),
        ),
    ]
