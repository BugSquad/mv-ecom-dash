from django.shortcuts import render

# Create your views here.

def products(request):
    """Products page.
    """
    return render(
        request,
        "products/mv_admin_products.html",
        {
            "nav_active": "products"
        }
    )

def categories(request):
    """Categories page.
    """
    return render(
        request,
        "products/mv_admin_products_categories.html",
        {
            "nav_active": "products categories"
        }
    )