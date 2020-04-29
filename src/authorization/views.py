from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

login_error = False
login_error_credentials = "Wrong email or password"
login_error_server = "Server error occured"


@csrf_protect
def signin(request):
    login_error = False
    if request.user.is_authenticated:
        return HttpResponseRedirect("/dashboard/")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        remember_me = request.POST.get("remember_me", False)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if remember_me:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(300)  # 5 minutes

            login(request, user)
            return redirect("/")
        else:
            login_error = True
            form = AuthenticationForm(request.POST)
            data = {
                "login_error": login_error,
                "login_error_message": _(login_error_credentials),
                "form": form,
            }
            return render(request, "authorization/login.html", data)
    else:
        form = AuthenticationForm()
        data = {
            "login_error": login_error,
            "login_error_message": _(login_error_server),
            "form": form,
        }
        return render(request, "authorization/login.html", data)
