from django.shortcuts import render

# Create your views here.

def companies(request):
    """Companies page.
    """
    return render(
        request,
        "companies/mv_admin_companies.html",
        {
            "nav_active": "companies"
        }
    )

def categories(request):
    """Categories page.
    """
    return render(
        request,
        "companies/mv_admin_companies_categories.html",
        {
            "nav_active": "companies categories"
        }
    )