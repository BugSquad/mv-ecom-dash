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

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns

import authorization.views as athviews
import baseview.views as bviews
import utils.views as uviews
import users.views as usviews
import services.views as srviews
import customers.views as cviews
import vendors.views as vdviews
import companies.views as cmviews
import products.views as prviews
import promotions.views as prmviews
import finance.views as fviews
import support.views as spviews
import security.views as secviews
import reports.views as rptviews

urlpatterns = [
    url(
        r"^(?P<filename>(robots.txt)|(humans.txt))$",
        bviews.robots_txt,
        name="robots-files",
    ),
    path('admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r"^i18n/", include("django.conf.urls.i18n")),   # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls',
                                    'jet-dashboard')),  # Django JET dashboard URLS

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

# handler400 = 'utils.views.error_400'
# handler403 = 'utils.views.error_403'
# handler404 = 'utils.views.error_404'
# handler500 = 'utils.views.error_500'
