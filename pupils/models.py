from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date, datetime

# Create your models here.


class Parent(models.Model):
    parent_fname = models.CharField(max_length=25, null=False, blank=False)
    parent_surname = models.CharField(max_length=25, null=False, blank=False)
    contact_no = models.BigIntegerField(null=False, blank=False)
    # user_info = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.parent_fname} {self.parent_surname}: {self.contact_no}'


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
    year_gp = models.CharField(max_length=1, choices=YEAR_GROUPS)

    def __str__(self):
        return f'{self.first_name_of_pupil} {self.surname_of_pupil}: {self.year_gp}'


class Breakfast(models.Model):

    breakfast_option = [
        ("", "")
    ]
    breakfast_start_date = models.DateField()
    breakfast_end_date = models.DateField()

    def breakfast_options_to_add(self):
        if self.breakfast_start_date.weekday() < 5:
            if (self.breakfast_start_date, self.breakfast_start_date) in self.breakfast_option:
                return self.breakfast_option
            else:
                option.append(self.breakfast_start_date, self.breakfast_start_date)
                return self.breakfast_option

        if self.breakfast_end_date.weekday() < 5:
            if (self.breakfast_end_date, breakfast_end_date) in self.breakfast_option:
                return self.breakfast_option
            else:
                option.append(breakfast_end_date, breakfast_end_date)
                return self.breakfast_option

        i = 0
        while i < 365:
            i += 1
            new_date = self.breakfast_start_date + timedelta(days=i)
            if new_date < end:
                if new_date.weekday() < 5:
                    if (new_date, new_date) in self.breakfast_option:
                        return self.breakfast_option
                    else:
                        self.breakfast_option.append(new_date)
        return option
    # breakfast_options_to_add(self.breakfast_start_date, self.breakfast_end_date, self.breakfast_option)
    # def breakfast_options_to_add(self):
    #     if self.breakfast_start_date.weekday() < 5:
    #         if (self.breakfast_start_date, self.breakfast_start_date) in breakfast_option:
    #             return breakfast_option
    #         else:
    #             breakfast_option.append(
    #                 self.breakfast_start_date, self.breakfast_start_date)

    #     if self.breakfast_end_date.weekday() < 5:
    #         breakfast_option.append(
    #             self.breakfast_start_date, self.breakfast_start_date)

    #     i = 0
    #     while i < 365:
    #         i += 1
    #         new_date = self.breakfast_start_date + timedelta(days=i)
    #         if new_date < self.breakfast_end_date:
    #             if new_date.weekday() < 5:
    #                 breakfast_option.append(new_date)
    #     return breakfast_option
    # breakfast_choice = models.CharField(max_length=1, choices=breakfast_option)

    # breakfast_options_to_add(self.breakfast_start_date, self.breakfast_end_date)

    def __str__(self):
        return f'{self.breakfast_option}'


# class Supper(models.Model):
#     supper_start_date = models.DateField(unique=True)
#     supper_end_date = models.DateField(unique=True)  
    
#     def supper_options_to_add(self):
#         supper_options = []
#         if self.supper_start_date.weekday() < 5:
#             supper_options.append(self.supper_start_date)

#         if self.supper_end_date.weekday() < 5:
#             supper_options.append(self.supper_end_date)

#         i = 0
#         while i < 365:
#             i += 1
#             new_date = self.supper_start_date + timedelta(days=i)
#             if new_date < self.supper_end_date:
#                 if new_date.weekday() < 5:
#                     supper_options.append(new_date)
#         return supper_options

#     def __str__(self):
#         return f'{self.supper_options}'


class BookClub(models.Model):
    pupil_name = models.ForeignKey(
        Pupil, on_delete=models.CASCADE)
    parent_name = models.ForeignKey(Parent, on_delete=models.CASCADE)
    if_breakfast = models.BooleanField(null=False, blank=False)
    if_supper = models.BooleanField(null=False, blank=False)
    monday = models.BooleanField(null=False, blank=False)
    tuesday = models.BooleanField(null=False, blank=False)
    wednesday = models.BooleanField(null=False, blank=False)
    thursday = models.BooleanField(null=False, blank=False)
    friday = models.BooleanField(null=False, blank=False)
    # supper = models.ForeignKey(Supper, on_delete=models.CASCADE)
    # breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE)
    confirmation = models.BooleanField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pupil_name}: booked on {self.created_on}'
