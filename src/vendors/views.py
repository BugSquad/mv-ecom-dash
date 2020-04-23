from django.shortcuts import render

# Create your views here.

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