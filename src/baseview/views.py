from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_GET
from django.utils.translation import activate, LANGUAGE_SESSION_KEY
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings

# Create your views here.

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def signout(request):
    logout(request)
    return redirect('/')