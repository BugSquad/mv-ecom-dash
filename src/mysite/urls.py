"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

import authorization.views
import baseview.views
import dashboard.views
import utils.views

urlpatterns = [
    url(r'^$', baseview.views.start, name='mv_admin_start'),
    path('forgot_password/', TemplateView.as_view(
        template_name="authorization/forgot_password.html"),
        name='mv_admin_forgot_password'
    ),
    
    url(r'^blank/$', utils.views.blank, name='mv_admin_blank'),
    url(r'^login/$', authorization.views.login, name='mv_admin_login'),
    url(r'^dashboard/$', dashboard.views.dashboard, name='mv_admin_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler400 = 'utils.views.error_400'
# handler403 = 'utils.views.error_403'
# handler404 = 'utils.views.error_404'
# handler500 = 'utils.views.error_500'