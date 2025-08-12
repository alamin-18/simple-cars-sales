from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class singUpForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(max_length=150)
        last_name = forms.CharField(max_length=150)
        email = forms.EmailField()
        
        model =User
        
        fields = ['username','first_name','last_name','email']
        

class ChangeProfile(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        
        fields = ['username','first_name','last_name','email']
       