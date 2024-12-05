from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record
from django import forms
from simplemathcaptcha.fields import MathCaptchaField

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import * #PasswordInput, TextInput

# Create a User /Register A User

class CreateUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    #'email'

    class Meta:
        model = User
        fields =['username','password1','password2']
    
    captcha = MathCaptchaField()

# Login A user
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    captcha = MathCaptchaField()

#ADD/CREATE RECORD
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

#UPDATE RECORD
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model  = Record 
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country'] 


 