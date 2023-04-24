from .models import Pupil, DateRequest
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class PupilForm(forms.ModelForm):
    class Meta:
        model = Pupil
        fields = (
            'confirmation',
            'first_name_of_pupil',
            'surname_of_pupil',
            'year_gp',
            'parent_name',
            'parent_contact',
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

    def __init__(self, *args, **kwargs):
        super(PupilForm, self).__init__(*args, **kwargs)
        self.fields['b_mon'].legend = "Select your regular slots"

    def clean_confirmation(self):
        confirmation = self.cleaned_data.get('confirmation')
        if confirmation is False:
            raise forms.ValidationError('This field is required')
        return confirmation


class EditPupilForm(forms.ModelForm):
    class Meta:
        model = Pupil
        fields = (
            'confirmation',
            'parent_contact',
            'contact_email_for_pupil',
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

    def clean_confirmation(self):
        confirmation = self.cleaned_data.get('confirmation')
        if confirmation is False:
            raise forms.ValidationError('This field is required')
        return confirmation


class DateRequestForm(forms.ModelForm):

    class Meta:
        model = DateRequest
        fields = (
            'date_request',
            'type_of_request',
            'confirmation',
        )
        widgets = {
            'date_request': DateInput(),
        }

    def clean_confirmation(self):
        confirmation = self.cleaned_data.get('confirmation')
        if confirmation is False:
            raise forms.ValidationError('This field is required')
        return confirmation
