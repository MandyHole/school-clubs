from .models import Breakfast
from django import forms

class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = ('breakfast_start_date', 'breakfast_end_date',)