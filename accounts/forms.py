from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    SetPasswordForm,
)
from django.contrib.auth import get_user_model
from django.forms import forms


User = get_user_model()


class UserLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(UserLoginForm, self).__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Username", "required": "True"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password", "required": "True"}
        )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "First Name", "required": "True"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Last Name", "required": "True"}
        )
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Username", "required": "True"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Email", "required": "True"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password", "required": "True"}
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Retype Password",
                "required": "True",
            }
        )


class ResetPasswordConfirmForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields["new_password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "New Password", "required": True}
        )
        self.fields["new_password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Retype New Password",
                "required": True,
            }
        )
