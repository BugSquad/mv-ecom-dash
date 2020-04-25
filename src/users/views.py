from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.

@staff_member_required(login_url='/login/?next=/users/')
def users(request):
    """Users page.
    """
    return render(
        request,
        "users/mv_admin_users.html",
        {
            "nav_active": "users"
        }
    )