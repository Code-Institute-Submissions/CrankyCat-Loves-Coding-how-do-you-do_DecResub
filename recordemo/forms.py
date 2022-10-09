from django import forms
from django.forms import ModelForm
from datetime import datetime

from .models import AddFeeling


class AddFeelingForm(forms.ModelForm):

    FEELING_TYPES = [
        ('happy', 'Happy'),
        ('excited', 'Excited'),
        ('calm', 'Calm'),
        ('disppointed', 'Disppointed'),
        ('anxious', 'Anxious'),
        ('angry', 'Angry'),
    ]

    user_profile = forms.CharField()
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

    class Meta:
        model = AddFeeling
        fields = [
            'user_profile',
            'date',
            'feelings',
            'details'
        ]
