from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.

@staff_member_required(login_url='/login/?next=/services/')
def services(request):
    """Services page.
    """
    return render(
        request,
        "services/mv_admin_services.html",
        {
            "nav_active": "services"
        }
    )

@staff_member_required(login_url='/login/?next=/srv-categories/')
def categories(request):
    """Categories page.
    """
    return render(
        request,
        "services/mv_admin_services_categories.html",
        {
            "nav_active": "services categories"
        }
    )

@staff_member_required(login_url='/login/?next=/srv-providers/')
def providers(request):
    """Providers page.
    """
    return render(
        request,
        "services/mv_admin_services_providers.html",
        {
            "nav_active": "services providers"
        }
    )