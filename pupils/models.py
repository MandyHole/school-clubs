from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date, datetime

# Create your models here.


class Parent(models.Model):
    parent_fname = models.CharField(max_length=25, null=False, blank=False)
    parent_surname = models.CharField(max_length=25, null=False, blank=False)
    contact = models.BigIntegerField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.parent_fname} {self.parent_surname}: {contact}'


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
    year = models.CharField(max_length=1, choices=YEAR_GROUPS)

    def __str__(self):
        return f'{self.first_name_of_pupil} {self.surname_of_pupil}: {year}'


class Breakfast(models.Model):
    breakfast_start_date = models.DateField(unique=True)
    breakfast_end_date = models.DateField(unique=True)  

    def breakfast_options_to_add(self):
        breakfast_options = []
        if self.breakfast_start_date.weekday() < 5:
            breakfast_options.append(self.breakfast_start_date)

        if self.breakfast_end_date.weekday() < 5:
            breakfast_options.append(self.breakfast_end_date)

        i = 0
        while i < 365:
            i += 1
            new_date = self.breakfast_start_date + timedelta(days=i)
            if new_date < self.breakfast_end_date:
                if new_date.weekday() < 5:
                    breakfast_options.append(new_date)
        return breakfast_options

    def __str__(self):
        return f'{self.breakfast_options}'


class Supper(models.Model):
    supper_start_date = models.DateField(unique=True)
    supper_end_date = models.DateField(unique=True)  
    
    def supper_options_to_add(self):
        supper_options = []
        if self.supper_start_date.weekday() < 5:
            supper_options.append(self.supper_start_date)

        if self.supper_end_date.weekday() < 5:
            supper_options.append(self.supper_end_date)

        i = 0
        while i < 365:
            i += 1
            new_date = self.supper_start_date + timedelta(days=i)
            if new_date < self.supper_end_date:
                if new_date.weekday() < 5:
                    supper_options.append(new_date)
        return supper_options

    def __str__(self):
        return f'{self.supper_options}'


class BookClub(models.Model):
    pupil_name = models.ForeignKey(
        Pupil, on_delete=models.CASCADE)
    parent_name = models.ForeignKey(Parent, on_delete=models.CASCADE)
    if_breakfast = models.BooleanField(default=False)
    if_supper = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    supper = models.ForeignKey(Supper, on_delete=models.CASCADE)
    breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE)
    confirmation = models.BooleanField(null=False, blank=False)
