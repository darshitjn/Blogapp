from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length= 60)
    last_name = forms.CharField(max_length= 60) 
    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','email')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field,value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

class UserEditForm(UserChangeForm):
    first_name = forms.CharField(max_length= 60)
    last_name = forms.CharField(max_length= 60) 
    password = None
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
    
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        for field,value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

class ChangePwdForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePwdForm, self).__init__(*args, **kwargs)
        for field,value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'   
            