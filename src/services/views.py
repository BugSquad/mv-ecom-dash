from django.shortcuts import render

# Create your views here.

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