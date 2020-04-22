from django.shortcuts import render

# Create your views here.

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