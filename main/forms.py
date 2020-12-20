from django import forms
from .models import Members
from bootstrap_datepicker_plus import DatePickerInput


class NewMember(forms.ModelForm):

    class Meta:
        model = Members
        fields = "__all__"
        widgets = {
            'Date_of_Birth': DatePickerInput(format='%Y-%m-%d'),
            'Date_registered': DatePickerInput(format='%Y-%m-%d'),
        }


form = NewMember()
