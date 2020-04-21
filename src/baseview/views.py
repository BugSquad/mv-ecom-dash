from django.shortcuts import render

# Create your views here.

def start(request):
    """Start page with a documentation.
    """
    return render(
        request,
        "baseview/start.html",
        {
            "nav_active": "start"
        }
    )
