from django import forms
from django.utils.translation import ugettext_lazy as _


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn't match."),
    }
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "id": "inputPassword",
                "name": "new_password",
                "class": "form-control",
                "placeholder": "Enter new password",
                "required": "required",
                "autofocus": "autofocus",
            }
        )
    )
    conf_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "id": "inputConf",
                "name": "conf_password",
                "class": "form-control",
                "placeholder": "Enter conf password",
                "required": "required",
                "autofocus": "autofocus",
            }
        )
    )

    def clean_new_password2(self):
        password = self.cleaned_data.get("new_password")
        conf_password = self.cleaned_data.get("conf_password")
        if password and conf_password:
            if password != conf_password:
                raise forms.ValidationError(
                    self.error_messages["password_mismatch"], code="password_mismatch",
                )
        return conf_password
