from django import forms
from .models import Wellness


class CheckinForm(forms.ModelForm):

    class Meta:
        model = Wellness
        fields = ('health_rating',)
        labels = {'health_rating': '(1-10)'}