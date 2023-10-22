from .models import Profile
from django import forms


class ProfileEditForm(forms.ModelForm):
   class Meta:
     model = Profile
     fields = ('date_of_birth', 'photo', 'phone_number', 'bio')

class ProfileEditForm(forms.ModelForm):
   class Meta:
      model = Profile
      fields = ('date_of_birth','photo','phone_number','bio')
