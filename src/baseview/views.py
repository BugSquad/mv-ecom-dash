from django.http import HttpResponseRedirect

# Create your views here.

def start(request):
    """Start at dashboard.
    """
    return HttpResponseRedirect('/dashboard/')
