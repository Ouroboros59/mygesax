from django import forms
from base.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = ['avatar']