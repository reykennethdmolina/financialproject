"""financial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

admin.site.index_template = 'admin/index.html'
admin.autodiscover()

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index2/', views.index2, name='index2'),
    url(r'^admin/', admin.site.urls),

    # Apps URLS
    url(r'^mainproduct/', include('mainproduct.urls', namespace='mainproduct')),
    url(r'^product/', include('product.urls', namespace='product')),

    # Apps Grace
    url(r'^vat/', include('vat.urls', namespace='vat')),
    url(r'^wtax/', include('wtax.urls', namespace='wtax')),
    url(r'^mainunit/', include('mainunit.urls', namespace='mainunit')),
    url(r'^unit/', include('unit.urls', namespace='unit')),
    url(r'^typeofexpense/', include('typeofexpense.urls', namespace='typeofexpense')),
    #url(r'^currency/', include('currency.urls', namespace='currency')),
    #url(r'^industry/', include('industry.urls', namespace='industry')),
    #url(r'^bankaccounttype/', include('bankaccounttype.urls', namespace='bankaccounttype')),
    #url(r'^bankaccount/', include('bankaccount.urls', namespace='bankaccount')),

    # Apps Kelvin
    url(r'^ataxcode/', include('ataxcode.urls', namespace='ataxcode')),
    url(r'^inputvat/', include('inputvat.urls', namespace='inputvat')),
    url(r'^inputvattype/', include('inputvattype.urls', namespace='inputvattype')),
    url(r'^kindofexpense/', include('kindofexpense.urls', namespace='kindofexpense')),
    url(r'^mistype/', include('mistype.urls', namespace='mistype')),
    url(r'^bank/', include('bank.urls', namespace='bank')),

    # Login/Logout URLs
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'next_page': '/login/'})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
