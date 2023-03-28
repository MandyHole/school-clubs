from .models import Pupil, Parent, DateRequest, Breakfast, BreakfastRequest
from django import forms
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = ('breakfast_start_date', 'breakfast_end_date',)


class PupilForm(forms.ModelForm):
    class Meta:
        model = Pupil
        fields = (
            'first_name_of_pupil',
            'surname_of_pupil',
            'year_gp',
            'b_mon',
            'b_tues',
            'b_wed',
            'b_thurs',
            'b_fri',
            's_mon',
            's_tues',
            's_wed',
            's_thurs',
            's_fri',
            )


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = (
            'parent_fname', 'parent_surname', 'contact_no',)


class EditParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = (
            'parent_fname', 'parent_surname', 'contact_no', 'parent_email',)


class SetBreakfastDates(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = (
            'breakfast_start_date', 'breakfast_end_date',
        )


class BreakfastRequestForm(forms.ModelForm):
    class Meta:
        model = BreakfastRequest
        fields = (
            'additional_breakfast',
            'cancel_breakfast',
            'additional_supper',
            'cancel_supper',
        )


class DateRequestForm(forms.ModelForm):

    class Meta:
        model = DateRequest
        fields = (
            'date_request',
            'type_of_request',
        )
        widgets = {
            'date_request': DateInput(),
        }
