from django.shortcuts import render

# Create your views here.

def blank(request):
    """Blank page.
    """
    return render(request, "utils/mv_admin_blank.html",
                  {"nav_active":"blank"})