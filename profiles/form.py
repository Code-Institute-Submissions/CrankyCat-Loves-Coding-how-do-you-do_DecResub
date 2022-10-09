from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    name = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ['name']
