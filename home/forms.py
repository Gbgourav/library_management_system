from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.forms import fields
from django.forms.widgets import Widget
from django.utils.translation import gettext, gettext_lazy as _

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.
    PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.
    PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.
    EmailInput(attrs={'class':'form-control'}))            
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email':'Email'}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
        
# I create a class by using inbult SignUpForm class to register user. it looks like models class but django provide some builtin 
# features to create login page, logout page and change passwored features I took one the SignUpForm class 
# I added some additinol fields like passwored confirmation and email. I userd bootstrap form class "form-control" this class give a good UI to the user.  

# I used UserCreationForm, AuthenticationForm, UsernameField. These are the inbuilt features of django. UserCreationForm is used for creating a 
# new user that can use our web application.AuthenticationForm gives permissions: Binary (yes/no) flags designating whether a user may perform a certain task.
# if user is authentacated it will allow user. AuthenticationForm it define the forms fields.

# "Widget" representation of an HTML input element and "fiels" is used data types to store a particular type of data. For example, to store an integer, IntegerField

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label =_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
                
            
            
# I created LoginForm class to login user in our app this is also a builtin feature of the django. I usered "form-control" 
# bootstrap class to give good UI for user
# gettext, gettext_lazy as _ func provide software internationalization. as I appied _('Password') that means passwred lanugage 
# sould be based on setting.py language.
           