from django import forms
from .models import Wellness


class CheckinForm(forms.ModelForm):

    class Meta:
        model = Wellness
        fields = ('health_rating',)
        labels = {'health_rating': 'How are you feeling on a scale of 1-10?'}