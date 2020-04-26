from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.

@staff_member_required(login_url='/login/?next=/promotions/')
def promotions(request):
    """Promotions page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions.html",
        {
            "nav_active": "promotions"
        }
    )

@staff_member_required(login_url='/login/?next=/prm-discounts/')
def discounts(request):
    """Discounts page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions_discounts.html",
        {
            "nav_active": "promotions"
        }
    )

@staff_member_required(login_url='/login/?next=/prm-promocodes/')
def promocodes(request):
    """Promocodes page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions_promos.html",
        {
            "nav_active": "promotions"
        }
    )

@staff_member_required(login_url='/login/?next=/prm-badges/')
def badges(request):
    """Badges page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions_badges.html",
        {
            "nav_active": "promotions"
        }
    )

@staff_member_required(login_url='/login/?next=/prm-advertising/')
def advertising(request):
    """Advertising page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions_advertising.html",
        {
            "nav_active": "promotions"
        }
    )