from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.

@staff_member_required(login_url='/login/?next=/vendors/')
def vendors(request):
    """Vendors page.
    """
    return render(
        request,
        "vendors/mv_admin_vendors.html",
        {
            "nav_active": "vendors"
        }
    )

@staff_member_required(login_url='/login/?next=/vendors-ratings/')
def ratings(request):
    """Ratings page.
    """
    return render(
        request,
        "vendors/mv_admin_vendors_ratings.html",
        {
            "nav_active": "vendors ratings"
        }
    )