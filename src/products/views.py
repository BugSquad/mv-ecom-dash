from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.


@staff_member_required(login_url="/login/?next=/products/")
def products(request):
    """Products page.
    """
    return render(
        request, "products/mv_admin_products.html", {"nav_active": "products"}
    )


@staff_member_required(login_url="/login/?next=/prd-categories/")
def categories(request):
    """Categories page.
    """
    return render(
        request,
        "products/mv_admin_products_categories.html",
        {"nav_active": "products"},
    )


@staff_member_required(login_url="/login/?next=/prd-ratings/")
def ratings(request):
    """Ratings page.
    """
    return render(
        request, "products/mv_admin_products_ratings.html", {"nav_active": "products"}
    )
