from django.shortcuts import render

# Create your views here.

def customers(request):
    """Customers page.
    """
    return render(
        request,
        "customers/mv_admin_customers.html",
        {
            "nav_active": "customers"
        }
    )