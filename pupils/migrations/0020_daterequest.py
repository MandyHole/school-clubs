# Generated by Django 3.2.18 on 2023-03-27 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0019_auto_20230327_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_request', models.DateField(blank=True, null=True, verbose_name='Date of Request')),
                ('type_of_request', models.CharField(choices=[('0', 'Request an additional breakfast'), ('1', 'Request an additional supper'), ('2', 'Cancel existing breakfast'), ('3', 'Cancel existing supper')], max_length=1)),
                ('approved', models.BooleanField(default=False)),
                ('request_date', models.DateTimeField(auto_now_add=True, verbose_name='Date request was made')),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pupils.pupil')),
            ],
        ),
    ]