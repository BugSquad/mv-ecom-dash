from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.

@staff_member_required(login_url='/login/?next=/finance/')
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

@staff_member_required(login_url='/login/?next=/fin-orders/')
def orders(request):
    """Orders page.
    """
    return render(
        request,
        "finance/mv_admin_finance_orders.html",
        {
            "nav_active": "finance"
        }
    )

@staff_member_required(login_url='/login/?next=/fin-payments/')
def payments(request):
    """Payments page.
    """
    return render(
        request,
        "finance/mv_admin_finance_payments.html",
        {
            "nav_active": "finance"
        }
    )

@staff_member_required(login_url='/login/?next=/fin-delivery/')
def delivery(request):
    """Delivery page.
    """
    return render(
        request,
        "finance/mv_admin_finance_delivery.html",
        {
            "nav_active": "finance"
        }
    )

@staff_member_required(login_url='/login/?next=/fin-returns/')
def returns(request):
    """Returns page.
    """
    return render(
        request,
        "finance/mv_admin_finance_returns.html",
        {
            "nav_active": "finance"
        }
    )

@staff_member_required(login_url='/login/?next=/fin-refunds/')
def refunds(request):
    """Refunds page.
    """
    return render(
        request,
        "finance/mv_admin_finance_refunds.html",
        {
            "nav_active": "finance"
        }
    )

@staff_member_required(login_url='/login/?next=/fin-methods/')
def methods(request):
    """Methods page.
    """
    return render(
        request,
        "finance/mv_admin_finance_methods.html",
        {
            "nav_active": "finance"
        }
    )