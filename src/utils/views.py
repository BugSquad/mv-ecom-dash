from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blank(request):
    """Blank page.
    """
    return render(request, "utils/mv_admin_blank.html",
                  {"nav_active":"blank"})

def error_400(request, exception):
        return HttpResponse(status=400)

def error_403(request,  exception):
        return HttpResponse(status=403)

def error_404(request,  exception):
        return HttpResponse(status=404)

def error_500(request):
        return HttpResponse(status=500)