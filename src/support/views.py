from django.shortcuts import render

# Create your views here.

def support(request):
    """Support page.
    """
    return render(
        request,
        "support/mv_admin_support.html",
        {
            "nav_active": "support"
        }
    )

def complaints(request):
    """Complaints page.
    """
    return render(
        request,
        "support/mv_admin_support_complaints.html",
        {
            "nav_active": "complaints"
        }
    )

def suggestions(request):
    """Suggestions page.
    """
    return render(
        request,
        "support/mv_admin_support_suggestions.html",
        {
            "nav_active": "suggestions"
        }
    )