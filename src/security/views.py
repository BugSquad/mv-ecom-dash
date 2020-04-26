from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.

@staff_member_required(login_url='/login/?next=/security/')
def security(request):
    """Security page.
    """
    return render(
        request,
        "security/mv_admin_security.html",
        {
            "nav_active": "security"
        }
    )

@staff_member_required(login_url='/login/?next=/sec-groups/')
def groups(request):
    """Groups page.
    """
    return render(
        request,
        "security/mv_admin_security_groups.html",
        {
            "nav_active": "security"
        }
    )

@staff_member_required(login_url='/login/?next=/sec-permissions/')
def permissions(request):
    """Permissions page.
    """
    return render(
        request,
        "security/mv_admin_security_permissions.html",
        {
            "nav_active": "security"
        }
    )