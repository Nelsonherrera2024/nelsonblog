from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from user.models import Profile


class SignUpForm(UserCreationForm):

    username = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))

    full_name = forms.CharField(help_text=None,
                                label=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Nombre de completo'}))

    email = forms.EmailField(label=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Correo'}))

    password1 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    password2 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))


    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            'password1',
            'password2',
        ]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.TextInput(attrs={'placeholder':'Nombre de usuario'}))

    password = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class UserForm(forms.ModelForm):

    username = forms.CharField(help_text=None,
                               label="Nombre de usuario")

    full_name = forms.CharField(help_text=None,
                               label="Nombre completo")

    email = forms.CharField(label="Correo")

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
        ]

class ProfileForm(forms.ModelForm):

    photo = forms.ImageField(label="Foto",
                             help_text=None,
                             required=False,
                             widget=forms.FileInput())

    profession = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Tu profesión'}))

    about = forms.CharField(help_text=None,
                                 label=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Más sobre ti'}))

    birthday = forms.CharField(help_text=None,
                                 label=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Tu cumpleaños'}))

    twitter = forms.CharField(help_text=None,
                                 label=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Tu red'}))
    linkedin = forms.CharField(help_text=None,
                                 label=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Red profesional'}))
    facebook = forms.CharField(help_text=None,
                                 label=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Tu perfil'}))


    class Meta:
        model = Profile
        fields = [
            'photo',
            'profession',
            'about',
            'birthday',
            'twitter',
            'linkedin',
            'facebook',
        ]
