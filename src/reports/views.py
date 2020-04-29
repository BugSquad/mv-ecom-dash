from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.


@staff_member_required(login_url="/login/?next=/reports/")
def reports(request):
    """Reports page.
    """
    return render(request, "reports/mv_admin_reports.html", {"nav_active": "reports"})
