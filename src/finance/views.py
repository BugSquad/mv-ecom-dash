from django.shortcuts import render

# Create your views here.

def finance(request):
    """Finance page.
    """
    return render(
        request,
        "finance/mv_admin_finance.html",
        {
            "nav_active": "finance"
        }
    )

def orders(request):
    """Orders page.
    """
    return render(
        request,
        "finance/mv_admin_finance_orders.html",
        {
            "nav_active": "orders"
        }
    )

def payments(request):
    """Payments page.
    """
    return render(
        request,
        "finance/mv_admin_finance_payments.html",
        {
            "nav_active": "payments"
        }
    )

def delivery(request):
    """Delivery page.
    """
    return render(
        request,
        "finance/mv_admin_finance_delivery.html",
        {
            "nav_active": "delivery"
        }
    )

def returns(request):
    """Returns page.
    """
    return render(
        request,
        "finance/mv_admin_finance_returns.html",
        {
            "nav_active": "returns"
        }
    )

def refunds(request):
    """Refunds page.
    """
    return render(
        request,
        "finance/mv_admin_finance_refunds.html",
        {
            "nav_active": "refunds"
        }
    )

def methods(request):
    """Methods page.
    """
    return render(
        request,
        "finance/mv_admin_finance_methods.html",
        {
            "nav_active": "payment methods"
        }
    )