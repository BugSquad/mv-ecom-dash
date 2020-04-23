from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_GET
from django.utils.translation import activate, LANGUAGE_SESSION_KEY
from django.shortcuts import redirect
from django.conf import settings

# Create your views here.

def start(request):
    """Start at dashboard.
    """
    return HttpResponseRedirect('/dashboard/')

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")