from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.


@staff_member_required(login_url="/login/?next=/dashboard/")
def dashboard(request):
    """Dashboard page.
    """
    return render(
        request, "dashboard/mv_admin_dashboard.html", {"nav_active": "dashboard"}
    )
