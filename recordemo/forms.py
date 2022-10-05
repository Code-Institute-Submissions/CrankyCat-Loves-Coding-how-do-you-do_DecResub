from django import forms
from datetime import datetime

class AddFeelingForm(forms.Form):

    FEELING_TYPES = [
        ('happy', 'Happy'),
        ('excited', 'Excited'),
        ('calm', 'Calm'),
        ('disppointed', 'Disppointed'),
        ('anxious', 'Anxious'),
        ('angry', 'Angry'),
    ]

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'max': datetime.now().date()
        })
    )
    feelings = forms.ChoiceField(choices=FEELING_TYPES)
    details = forms.CharField(
        widget=forms.Textarea(),
    )