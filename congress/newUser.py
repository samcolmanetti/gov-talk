from django.contrib.auth.models import User
from django.forms import ModelForm
import models

class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'username', 'email', 'password'}
        
class UserProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = {'address'}