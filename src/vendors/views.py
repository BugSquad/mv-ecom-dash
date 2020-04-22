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