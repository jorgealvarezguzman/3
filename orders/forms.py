from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username',
                'first_name',
                'last_name',
                'email',)
        help_texts = {key:"" for key in fields}
