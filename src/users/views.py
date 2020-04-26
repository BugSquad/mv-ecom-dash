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

@staff_member_required(login_url='/login/?next=/us-profile/')
def user_profile(request):
    """Profile page.
    """
    return render(
        request,
        "users/mv_admin_users_profile.html",
        {
            "nav_active": "users"
        }
    )

@staff_member_required(login_url='/login/?next=/us-settings/')
def user_settings(request):
    """Settings page.
    """
    return render(
        request,
        "users/mv_admin_users_settings.html",
        {
            "nav_active": "users"
        }
    )

@staff_member_required(login_url='/login/?next=/us-logs/')
def user_logs(request):
    """Logs page.
    """
    return render(
        request,
        "users/mv_admin_users_logs.html",
        {
            "nav_active": "users"
        }
    )