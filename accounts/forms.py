from django import forms
from .models import User, Profile

class RegistrationForm(forms.ModelForm):

    name = forms.CharField(label='Enter Name',min_length=4,max_length=50,help_text='Required')
    username = forms.CharField(label='Enter Username',min_length=4,max_length=50,help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email','name')
        widgets = {
            'name':forms.TextInput(attrs={
                'type':'text',
                'autocomplete':'off',
                'class':'person_surname',
                'id':'person_surname',
                
            }),

            'email':forms.EmailInput(attrs={
                'type':'email',
                'autocomplete':'off',
                'class':'person_firstname',
                'id':'person_surname',
                
            }),

            'username':forms.TextInput(attrs={
                'type':'text',
                'autocomplete':'off',
                'class':'person_firstname',
                'id':'person_surname',
                
            }),
            
            'password':forms.PasswordInput(attrs={
                'type':'password',
                'autocomplete':'off',
                'class':'person_psa',
                'id':'psa',
                
            }),
        }    

    def save(self,commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user     

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter Full name'})    




""" LOGIN FORM """            
class LoginForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'Email address'}))        
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Password', 'id':'password'}))
