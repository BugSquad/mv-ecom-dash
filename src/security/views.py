from django.shortcuts import render

# Create your views here.

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

def groups(request):
    """Groups page.
    """
    return render(
        request,
        "security/mv_admin_security_groups.html",
        {
            "nav_active": "security groups"
        }
    )

def permissions(request):
    """Permissions page.
    """
    return render(
        request,
        "security/mv_admin_security_permissions.html",
        {
            "nav_active": "security permissions"
        }
    )