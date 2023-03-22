from .models import Breakfast, Pupil, Parent
from django import forms


class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = ('breakfast_start_date', 'breakfast_end_date',)


class PupilForm(forms.ModelForm):
    class Meta:
        model = Pupil
        fields = ('first_name_of_pupil', 'surname_of_pupil', 'year_gp',)


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = (
            'parent_fname', 'parent_surname', 'contact_no',)


class EditParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = (
            'parent_fname', 'parent_surname', 'contact_no', 'parent_email')