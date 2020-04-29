from django import forms


class PasswordResetRequestForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "id": "inputEmail",
                "name": "reset_email",
                "class": "form-control",
                "placeholder": "Enter email address",
                "required": "required",
                "autofocus": "autofocus",
            }
        )
    )
