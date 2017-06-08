"""work_site URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from tastypie.api import Api
from sectors.api.resources import CvsResource

v1_api = Api(api_name='v1')
v1_api.register(CvsResource())

from . import views

urlpatterns = [
    url(r'^job_categories/', include('sectors.urls', namespace='sectors')),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', views.IndexView),

    url(r'^$', views.hello_world),
    url(r'^api/', include(v1_api.urls)),
]

urlpatterns += staticfiles_urlpatterns()