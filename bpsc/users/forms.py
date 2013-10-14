from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SCUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SCUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].label = 'Email'

    class Meta:
        model = User
        fields = ('username', 'email',)
