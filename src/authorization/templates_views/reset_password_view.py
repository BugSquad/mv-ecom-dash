from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.views.generic import FormView
from authorization.forms.reset_password_form import PasswordResetRequestForm
from django.conf import settings
from authorization.models import MvUser
from django.db.models.query_utils import Q
from django.utils.translation import ugettext_lazy as _

class ResetPasswordRequestView(FormView):
    success_url = '/login'
    form_class = PasswordResetRequestForm

    messages = {
        'status': '',
        'message':'',
    }

    @staticmethod
    def validate_email_address(email):
        '''
        This method here validates the if the input is an email address or not. Its return type is boolean, True if the input is a email address or False if its not.
        '''
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def post(self, request, *args, **kwargs):
        '''
        A normal post request which takes input from field "email_or_username" (in ResetPasswordRequestForm).
        '''
        form = self.form_class(request.POST)
        if form.is_valid():
            data= form.cleaned_data["email"]
        if self.validate_email_address(data) is True:
            '''
            If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
            '''
            associated_users= MvUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    c = {
                        'email': user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'your site',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        }

                    subject_template_name='authorization/password_reset_subject.txt'
                    email_template_name='authorization/password_reset_email.html'
                    subject = loader.render_to_string(subject_template_name, c)
                    subject = ''.join(subject.splitlines())
                    email = loader.render_to_string(email_template_name, c)
                    send_mail(subject, email, settings.DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)

            self.messages.status = 'success'
            self.messages.message = _('An email has been sent to ') + data + _('. Please check your inbox to continue reseting password.')
            return self.form_valid(form)
        
        self.messages.status = 'failed'
        self.messages.message = _('Please enter a valid email address')
        return self.form_invalid(form)