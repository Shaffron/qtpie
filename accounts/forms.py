from django.forms import (
    ModelForm,
    PasswordInput
)

from accounts.models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        widget = {
            'password': PasswordInput()
        }
        