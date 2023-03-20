from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

from DjangoPetstagram.accounts.models import UserProfile

user_model = get_user_model()

class AppRegisterForm(UserCreationForm):
    class Meta:
        model = user_model
        fields = (user_model.USERNAME_FIELD, 'email', 'password1', 'password2')



class EditUserProfileForm(forms.ModelForm):
    EMAIL_MAX_LENGTH = 254
    email = forms.CharField(
        max_length=EMAIL_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'EMAIL',
            }
        ),
        validators=(validators.EmailValidator(), ),
    )

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'gender', 'profile_picture', 'email')



