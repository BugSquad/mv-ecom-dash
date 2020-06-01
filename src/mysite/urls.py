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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns

import authorization.views as athviews
import baseview.views as bviews
import dashboard.views as dviews
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

from authorization.templates_views.reset_password_view import ResetPasswordRequestView
from authorization.templates_views.change_password_view import PasswordResetConfirmView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(
        r"^(?P<filename>(robots.txt)|(humans.txt))$",
        bviews.robots_txt,
        name="robots-files",
    ),
    url(r"^i18n/", include("django.conf.urls.i18n")),
    url(r"^blank/$", uviews.blank, name="mv_admin_blank"),
    path(
        "forgot_password/",
        ResetPasswordRequestView.as_view(
            template_name="authorization/forgot_password.html"
        ),
        name="mv_admin_forgot_password",
    ),
    url(r"^$", athviews.signin, name="mv_admin_start"),
    url(r"^login/$", athviews.signin, name="mv_admin_login"),
    url(
        r"^change_password/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$",
        PasswordResetConfirmView.as_view(
            template_name="authorization/change_password.html"
        ),
        name="mv_admin_change_pass",
    ),
    url(r"^logout/$", bviews.signout, name="mv_admin_logout"),
    url(r"^dashboard/$", dviews.dashboard, name="mv_admin_dashboard"),
    url(r"^users/$", usviews.users, name="mv_admin_users"),
    url(r"^us-profile/$", usviews.user_profile, name="mv_admin_us_profile"),
    url(r"^us-settings/$", usviews.user_settings, name="mv_admin_us_settings"),
    url(r"^us-logs/$", usviews.user_logs, name="mv_admin_us_logs"),
    url(r"^services/$", srviews.services, name="mv_admin_services"),
    url(r"^srv-categories/$", srviews.categories, name="mv_admin_srv_categories"),
    url(r"^srv-providers/$", srviews.providers, name="mv_admin_srv_providers"),
    url(r"^customers/$", cviews.customers, name="mv_admin_customers"),
    url(r"^vendors/$", vdviews.vendors, name="mv_admin_vendors"),
    url(r"^vnd-ratings/$", vdviews.ratings, name="mv_admin_vnd_ratings"),
    url(r"^companies/$", cmviews.companies, name="mv_admin_companies"),
    url(r"^cmp-categories/$", cmviews.categories, name="mv_admin_cmp_categories"),
    url(r"^products/$", prviews.products, name="mv_admin_products"),
    url(r"^prd-categories/$", prviews.categories, name="mv_admin_prd_categories"),
    url(r"^prd-ratings/$", prviews.ratings, name="mv_admin_prd_ratings"),
    url(r"^prd-specs/$", prviews.specs, name="mv_admin_prd_specs"),
    url(r"^promotions/$", prmviews.promotions, name="mv_admin_promotions"),
    url(r"^prm-discounts/$", prmviews.discounts, name="mv_admin_prm_discounts"),
    url(r"^prm-promocodes/$", prmviews.promocodes,
        name="mv_admin_prm_promocodes"),
    url(r"^prm-badges/$", prmviews.badges, name="mv_admin_prm_badges"),
    url(r"^prm-advertising/$", prmviews.advertising,
        name="mv_admin_prm_advertising"),
    url(r"^finance/$", fviews.finance, name="mv_admin_finance"),
    url(r"^fin-orders/$", fviews.orders, name="mv_admin_fin_orders"),
    url(r"^fin-payments/$", fviews.payments, name="mv_admin_fin_payments"),
    url(r"^fin-delivery/$", fviews.delivery, name="mv_admin_fin_delivery"),
    url(r"^fin-returns/$", fviews.returns, name="mv_admin_fin_returns"),
    url(r"^fin-refunds/$", fviews.refunds, name="mv_admin_fin_refunds"),
    url(r"^fin-methods/$", fviews.methods, name="mv_admin_fin_methods"),
    url(r"^support/$", spviews.support, name="mv_admin_support"),
    url(r"^spt-complaints/$", spviews.complaints, name="mv_admin_spt_complaints"),
    url(r"^spt-suggestions/$", spviews.suggestions,
        name="mv_admin_spt_suggestions"),
    url(r"^security/$", secviews.security, name="mv_admin_security"),
    url(r"^sec-groups/$", secviews.groups, name="mv_admin_sec_groups"),
    url(r"^sec-permissions/$", secviews.permissions,
        name="mv_admin_sec_permissions"),
    url(r"^reports/$", rptviews.reports, name="mv_admin_reports"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

# handler400 = 'utils.views.error_400'
# handler403 = 'utils.views.error_403'
# handler404 = 'utils.views.error_404'
# handler500 = 'utils.views.error_500'
