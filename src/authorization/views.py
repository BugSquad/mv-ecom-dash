from django.shortcuts import render

# Create your views here.

def login(request):
    """Start page with a documentation.
    """
    return render(
        request,
        "authorization/login.html"
    )