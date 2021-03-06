from django import forms
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
class AddAdmin(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password', 'remember_me']

        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter your username'
            }),
            'password':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter your password',
                'type':'password',
                'name':'password',
                'id':'password',
                'aria-describedby':'password'
            }),
            'remember_me':forms.CheckboxInput(attrs={
                'class':'form-check-input'
            })
        }



class PositionForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['section','position', 'user', 'author', 'country']

        def __init__(self, user, **kwargs) -> None:
            super(PositionForm, self).__init__(**kwargs)
            if user:
                self.fields['section'].queryset = Employe.objects.create(user=user)



class AdminChange(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['first_name', 'last_name', 'email', 'bio','adress', 'status', 'gender','position', 'section']

        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'bio':forms.Textarea(attrs={
                'class':'form-control',
                'type':'text',
                'name':'text'
            }),
            'adress':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'gender':forms.Select(attrs={
                'class':'form-control'
            }),
            'position':forms.Select(attrs={
                'class':'form-control'
            }),
            'section':forms.Select(attrs={
                'class':'form-control'
            })
        }
class AddUser(forms.ModelForm):
    class Meta:
        model = AdduserCount
        fields = ['users']

class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})