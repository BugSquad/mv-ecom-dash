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
import users.views
import services.views
import customers.views
import vendors.views
import companies.views
import products.views
import promotions.views
import finance.views
import support.views
import security.views
import reports.views

urlpatterns = [
    url(r'^$', baseview.views.start, name='mv_admin_start'),
    path('forgot_password/', TemplateView.as_view(
        template_name="authorization/forgot_password.html"),
        name='mv_admin_forgot_password'
    ),
    
    url(r'^blank/$', utils.views.blank, name='mv_admin_blank'),
    url(r'^login/$', authorization.views.login, name='mv_admin_login'),
    url(r'^dashboard/$', dashboard.views.dashboard, name='mv_admin_dashboard'),

    url(r'^users/$', users.views.users, name='mv_admin_users'),

    url(r'^services/$', services.views.services, name='mv_admin_services'),
    url(r'^srv-categories/$', services.views.categories, name='mv_admin_srv_categories'),
    url(r'^srv-providers/$', services.views.providers, name='mv_admin_srv_providers'),

    url(r'^customers/$', customers.views.customers, name='mv_admin_customers'),
    url(r'^vendors/$', vendors.views.vendors, name='mv_admin_vendors'),

    url(r'^companies/$', companies.views.companies, name='mv_admin_companies'),
    url(r'^cmp-categories/$', companies.views.categories, name='mv_admin_cmp_categories'),

    url(r'^products/$', products.views.products, name='mv_admin_products'),
    url(r'^prd-categories/$', products.views.categories, name='mv_admin_prd_categories'),

    url(r'^promotions/$', promotions.views.promotions, name='mv_admin_promotions'),
    url(r'^prm-discounts/$', promotions.views.discounts, name='mv_admin_prm_discounts'),
    url(r'^prm-promocodes/$', promotions.views.promocodes, name='mv_admin_prm_promocodes'),
    url(r'^prm-badges/$', promotions.views.badges, name='mv_admin_prm_badges'),
    url(r'^prm-advertising/$', promotions.views.advertising, name='mv_admin_prm_advertising'),

    url(r'^finance/$', finance.views.finance, name='mv_admin_finance'),
    url(r'^fin-orders/$', finance.views.orders, name='mv_admin_fin_orders'),
    url(r'^fin-payments/$', finance.views.payments, name='mv_admin_fin_payments'),
    url(r'^fin-delivery/$', finance.views.delivery, name='mv_admin_fin_delivery'),
    url(r'^fin-returns/$', finance.views.returns, name='mv_admin_fin_returns'),
    url(r'^fin-refunds/$', finance.views.refunds, name='mv_admin_fin_refunds'),
    url(r'^fin-methods/$', finance.views.methods, name='mv_admin_fin_methods'),

    url(r'^support/$', support.views.support, name='mv_admin_support'),
    url(r'^spt-complaints/$', support.views.complaints, name='mv_admin_spt_complaints'),
    url(r'^spt-suggestions/$', support.views.suggestions, name='mv_admin_spt_suggestions'),

    url(r'^security/$', security.views.security, name='mv_admin_security'),
    url(r'^sec-groups/$', security.views.groups, name='mv_admin_sec_groups'),
    url(r'^sec-permissions/$', security.views.permissions, name='mv_admin_sec_permissions'),

    url(r'^reports/$', reports.views.reports, name='mv_admin_reports'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler400 = 'utils.views.error_400'
# handler403 = 'utils.views.error_403'
# handler404 = 'utils.views.error_404'
# handler500 = 'utils.views.error_500'