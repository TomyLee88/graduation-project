from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'custom-date-input', 'type': 'date'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create Event'))

    
class UserSearchForm(forms.Form):
    query = forms.CharField(label='Search')        