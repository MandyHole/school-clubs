from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pupil(models.Model):
    YEAR_GROUPS = (
        ('0', 'Reception'),
        ('1', 'Year 1'),
        ('2', 'Year 2'),
        ('3', 'Year 3'),
        ('4', 'Year 4'),
        ('5', 'Year 5'),
        ('6', 'Year 6'),
    )
    first_name_of_pupil = models.CharField(
        max_length=25, null=False, blank=False)
    surname_of_pupil = models.CharField(max_length=25, null=False, blank=False)
    # parent_name = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_email = models.EmailField(max_length=254)
    year_group = models.CharField(max_length=1, choices=YEAR_GROUPS)

    def __str__(self):
        return f'{self.first_name_of_pupil} {self.surname_of_pupil}'


class Breakfast(models.Model):
    pupil_name = models.ForeignKey(
        Pupil, on_delete=models.CASCADE, unique_for_date='breakfast_date')
    breakfast_date = models.DateField()
    # confirmation = models.BooleanField()

    def __str__(self):
        return f'{self.pupil_name}: {self.breakfast_date}'


class Supper(models.Model):
    pupil_name = models.ForeignKey(
        Pupil, on_delete=models.CASCADE, unique_for_date='supper_date')
    supper_date = models.DateField()
    # confirmation = models.BooleanField()

    def __str__(self):
        return f'{self.pupil_name}: {self.supper_date}'
