from django.views.generic import FormView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from authorization.forms.change_password_form import SetPasswordForm
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class PasswordResetConfirmView(FormView):
    success_url = "/login/"
    form_class = SetPasswordForm

    messages = {
        "status": "",
        "message": "",
    }

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """
        UserModel = get_user_model()
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password = form.cleaned_data["conf_password"]
                user.set_password(new_password)
                user.save()

                self.messages.status = "success"
                self.messages.messages = _("Password has been reset.")
                return self.form_valid(form)
            else:
                self.messages.status = "failed"
                self.messages.messages = _("Password reset failed..")
                return self.form_invalid(form)
        else:
            self.messages.status = "failed"
            self.messages.messages = _("The reset password link is no longer valid.")
            return self.form_invalid(form)
