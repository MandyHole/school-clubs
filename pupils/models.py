from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date, datetime
from django.core.exceptions import ValidationError

# Create your models here.


class Parent(models.Model):
    parent_fname = models.CharField(
        max_length=25,
        null=False, blank=False, verbose_name="Your first name")
    parent_surname = models.CharField(
        max_length=25, null=False, blank=False, verbose_name="Your surname")
    contact_no = models.CharField(
        max_length=12,
        null=False, blank=False, verbose_name="Your contact number")
    parent_email = models.EmailField()
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)

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
    APPROVAL_OPTIONS = (
        ('0', 'Pending Approval'),
        ('1', 'Approved')
    )
    first_name_of_pupil = models.CharField(
        max_length=25, null=False, blank=False)
    surname_of_pupil = models.CharField(max_length=25, null=False, blank=False)
    year_gp = models.CharField(
        max_length=1, choices=YEAR_GROUPS, verbose_name="Year group")
    parent_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Name of parent making booking")
    parent_contact = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        verbose_name="Parent's preferred contact number"
    )
    user_info = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_email_for_pupil = models.EmailField()
    b_mon = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Monday Breakfast")
    b_tues = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Tuesday Breakfast")
    b_wed = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Wednesday Breakfast")
    b_thurs = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Thursday Breakfast")
    b_fri = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Friday Breakfast")
    s_mon = models.BooleanField(
        null=False, blank=False, default=False, verbose_name="Monday Supper")
    s_tues = models.BooleanField(
        null=False, blank=False, default=False, verbose_name="Tuesday Supper")
    s_wed = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name="Wednesday Supper")
    s_thurs = models.BooleanField(
        null=False, blank=False, default=False, verbose_name="Thursday Supper")
    s_fri = models.BooleanField(
        null=False, blank=False, default=False, verbose_name="Friday Supper")
    confirmation = models.BooleanField(
        verbose_name='I am aware it is £2/Breakfast and £2.50/Supper',
        default=True,
        null=False,
        blank=False,
        # validators=[confirmation_check()]
    )
    booking_approval_status = models.CharField(
        max_length=1,
        choices=APPROVAL_OPTIONS,
        verbose_name="Approval status",
        default='0')

    def __str__(self):
        return f'{self.first_name_of_pupil} {self.surname_of_pupil}'


def confirmation_check(value):
    if value is False:
        raise ValidationError(
            _('You must tick to confirm'),
            params={'value': value},
            )


class Breakfast(models.Model):

    # breakfast_option = models.DateField()
    breakfast_start_date = models.DateField()
    breakfast_end_date = models.DateField()


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


class BreakfastRequest(models.Model):
    additional_breakfast = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date of additional breakfast (if applicable)")
    cancel_breakfast = models.DateField(
        null=True,
        blank=True,
        verbose_name="Breakfast date you no longer require (if applicable)")
    approved = models.BooleanField(null=False, blank=False, default=False)
    additional_supper = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date of additional supper (if applicable)")
    cancel_supper = models.DateField(
        null=True,
        blank=True,
        verbose_name="Supper date you no longer require (if applicable)")
    request_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date request was made")
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)


class DateRequest(models.Model):
    date_request = models.DateField(verbose_name="Date of Request")
    REQUEST_TYPES = (
        ('0', 'Additional breakfast'),
        ('1', 'Additional supper'),
        ('2', 'Cancel breakfast'),
        ('3', 'Cancel supper'),
        )
    APPROVAL_CHOICES = (
        ('0', 'Awaiting Approval'),
        ('1', 'Approved'),
        ('2', 'Declined: Club unavailable on requested date'),
        ('3', 'Declined: Insufficient notice')
    )
    DECLINED_REASONING = (
        ('0', 'Awaiting Decision'),
        ('1', 'Club unavailable on requested date'),
        ('2', 'Insufficient notice')
    )
    approval_status = models.CharField(
        max_length=2, choices=APPROVAL_CHOICES, default='0')
    why_declined = models.CharField(
        max_length=2, choices=DECLINED_REASONING, default='0'
    )
    type_of_request = models.CharField(
        max_length=2, choices=REQUEST_TYPES)
    approved = models.BooleanField(null=False, blank=False, default=False)
    request_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date request was made")
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
