from django.shortcuts import render

# Create your views here.

def reports(request):
    """Reports page.
    """
    return render(
        request,
        "reports/mv_admin_reports.html",
        {
            "nav_active": "reports"
        }
    )