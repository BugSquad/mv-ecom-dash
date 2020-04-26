from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.

@staff_member_required(login_url='/login/?next=/support/')
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

@staff_member_required(login_url='/login/?next=/spt-complaints/')
def complaints(request):
    """Complaints page.
    """
    return render(
        request,
        "support/mv_admin_support_complaints.html",
        {
            "nav_active": "support"
        }
    )

@staff_member_required(login_url='/login/?next=/spt-suggestions/')
def suggestions(request):
    """Suggestions page.
    """
    return render(
        request,
        "support/mv_admin_support_suggestions.html",
        {
            "nav_active": "support"
        }
    )