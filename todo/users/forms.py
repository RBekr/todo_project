from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from base.models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

class LoginUserForm(AuthenticationForm):
    pass