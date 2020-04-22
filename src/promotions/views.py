from django.shortcuts import render

# Create your views here.

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

def discounts(request):
    """Discounts page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions_discounts.html",
        {
            "nav_active": "discounts"
        }
    )

def promocodes(request):
    """Promocodes page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions_promos.html",
        {
            "nav_active": "promocodes"
        }
    )

def badges(request):
    """Badges page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions_badges.html",
        {
            "nav_active": "badges"
        }
    )

def advertising(request):
    """Advertising page.
    """
    return render(
        request,
        "promotions/mv_admin_promotions_advertising.html",
        {
            "nav_active": "advertising"
        }
    )