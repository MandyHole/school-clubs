# Generated by Django 3.2.18 on 2023-03-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0006_remove_breakfast_breakfast_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfast',
            name='breakfast_end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='breakfast',
            name='breakfast_start_date',
            field=models.DateField(),
        ),
    ]