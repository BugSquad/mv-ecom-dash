from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Create your views here.


@staff_member_required(login_url="/login/?next=/customers/")
def customers(request):
    """Customers page.
    """
    return render(
        request, "customers/mv_admin_customers.html", {"nav_active": "customers"}
    )
