from django.shortcuts import render

# Create your views here.

def blank(request):
    """Blank page.
    """
    return render(request, "utils/mv_admin_blank.html",
                  {"nav_active":"blank"})

def error_400(request, exception):
        data = {"nav_active":"bad_request"}
        return render(request, 'utils/mv_admin_400.html', data)

def error_403(request,  exception):
        data = {"nav_active":"forbidden"}
        return render(request, 'utils/mv_admin_403.html', data)

def error_404(request,  exception):
        data = {"nav_active":"not_found"}
        return render(request, 'utils/mv_admin_404.html', data)

def error_500(request):
        data = {"nav_active":"server_error"}
        return render(request, 'utils/mv_admin_500.html', data)