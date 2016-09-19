"""gde URL Configuration

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
from app.views import *
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from app.views import *

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^register/$', cadastroUsuario),
                  url(r'^home/$', home),
                  url(r'^user/(?P<pk>[\d]+)/$', user_detail),
                  url(r'^$', auth_views.login, {'template_name': 'login.html'}),
                  url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
                  url(r'^especieDocumental/$', especieDocumental),
                  url(r'^especieDocumental/(?P<pk>\d+)/edit/$', especieDocumental_edit, name='especieDocumental_edit'),
                  url(r'^especiesDocumentais_list/$', especiesDocumentais_list),
                  url(r'^especieDocumental/(?P<pk>\d+)/remove/$', especieDocumental_remove, name='especieDocumental_remove'),
                  url(r'^setor/$', setor),
                  url(r'^setores_list/$', setores_list),
                  url(r'^setor/(?P<pk>\d+)/edit/$', setor_edit, name='setor_edit'),
                  url(r'^setor/(?P<pk>\d+)/remove/$', setor_remove, name='setor_remove'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

