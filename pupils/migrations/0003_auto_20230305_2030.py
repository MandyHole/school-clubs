# Generated by Django 3.2.18 on 2023-03-05 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0002_auto_20230305_2029'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookClub',
        ),
        migrations.DeleteModel(
            name='Breakfast',
        ),
        migrations.DeleteModel(
            name='Pupil',
        ),
        migrations.DeleteModel(
            name='Supper',
        ),
    ]
