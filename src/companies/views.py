from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.


@staff_member_required(login_url="/login/?next=/companies/")
def companies(request):
    """Companies page.
    """
    return render(
        request, "companies/mv_admin_companies.html", {"nav_active": "companies"}
    )


@staff_member_required(login_url="/login/?next=/cmp-categories/")
def categories(request):
    """Categories page.
    """
    return render(
        request,
        "companies/mv_admin_companies_categories.html",
        {"nav_active": "companies"},
    )
