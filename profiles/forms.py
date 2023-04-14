from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['story', 'is_anonymous', 'force', 'regiment', 'rank']

