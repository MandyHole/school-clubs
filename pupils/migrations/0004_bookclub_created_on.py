# Generated by Django 3.2.18 on 2023-03-06 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0003_auto_20230306_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookclub',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
