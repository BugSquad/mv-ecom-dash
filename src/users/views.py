from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.


@staff_member_required(login_url="/login/?next=/users/")
def users(request):
    """Users page.
    """
    return render(request, "users/mv_admin_users.html", {"nav_active": "users"})


@staff_member_required(login_url="/login/?next=/us-profile/")
def user_profile(request):
    """Profile page.
    """
    context = {
        "nav_active": "users",
        "user":request.user
    }
    return render(request, "users/mv_admin_users_profile.html", context)

@staff_member_required(login_url="/login/?next=/us-settings/")
def user_settings(request):
    """Settings page.
    """
    return render(
        request, "users/mv_admin_users_settings.html", {"nav_active": "users"}
    )

@staff_member_required(login_url="/login/?next=/us-logs/")
def user_logs(request):
    """Logs page.
    """
    return render(request, "users/mv_admin_users_logs.html", {"nav_active": "users"})

@staff_member_required(login_url="/login/?next=/us-logs/")
def user_create(request):
    """Create User page.
    """
    return render(request, "users/mv_admin_users_edit.html", {"nav_active": "users"})
