from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
import models

class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'username', 'email', 'password'}
        widgets = {
            'password': forms.PasswordInput(),
        }
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password']
            
            
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
        
class UserProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = {'address'}