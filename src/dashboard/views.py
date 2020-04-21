from django.shortcuts import render

# Create your views here.

def dashboard(request):
    """Dashboard page.
    """
    return render(
        request,
        "dashboard/mv_admin_dashboard.html",
        {
            "nav_active": "dashboard"
        }
    )