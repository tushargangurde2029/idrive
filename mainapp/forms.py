from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from mainapp.models import User_Data,Drive_Data

gen=[
    ('Male','Male'),
    ('Female','Female')
]

class Create_User(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class Create_User1(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class Register_Form(forms.ModelForm):
    gender=forms.CharField(widget=forms.RadioSelect(choices=gen),required=True)
    class Meta:
        model = User_Data
        fields = ['mobile_number','gender','image','temail']

class Register_Form1(forms.ModelForm):
    gender=forms.CharField(widget=forms.RadioSelect(choices=gen),required=True)
    class Meta:
        model = User_Data
        fields = ['mobile_number','gender']


class File_Form(forms.ModelForm):
    class Meta:
        model = Drive_Data
        fields = '__all__'