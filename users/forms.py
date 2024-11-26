from django import forms
from .models import Users


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)



class IshtirokchiForm(forms.ModelForm):
    username = forms.CharField(max_length=14, label='JSHR', min_length=14)
    last_name = forms.CharField(max_length=255, label='Familya')
    first_name = forms.CharField(max_length=255, label='Ism')
    password = forms.CharField(max_length=9, label='Parol', min_length=9)

    class Meta:
        model = Users
        fields = fields = ['username', 'last_name', 'first_name', 'password']