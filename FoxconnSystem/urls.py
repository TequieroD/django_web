"""FoxconnSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from activity import views as activity_views
from authorization import views as auth_views
#from activity.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login),
    url(r'^activity/summary/$', activity_views.summary),
    url(r'^activity/info/$', activity_views.info),
    url(r'^activity/registration/$', activity_views.registration),
    url(r'^activity/([^/]+)/delete/$', activity_views.delete),
    url(r'^activity/([^/]+)/signUpDelete/$', activity_views.signUpDelete),
    url(r'^activity/([^/]+)/update/$', activity_views.update),
    #url(r'^activity/create/$', activity_views.create),
    url(r'^activity/signuplist/$', activity_views.signUpList),
    url(r'^activity/list/$', activity_views.list),
    url(r'^activity/signUpReg/$', activity_views.signUpReg),
    url(r'^activity/([^/]+)/signUpUpdate/$', activity_views.signUpUpdate),

    url(r'^auth/authList/$', auth_views.authList),
    url(r'^auth/authReg/$', auth_views.authReg),
    url(r'^auth/([^/]+)/authUpdate/$', auth_views.authUpdate),
    url(r'^auth/([^/]+)/authDelete/$', auth_views.authDelete),
    url(r'^auth/create/$', auth_views.create_accont),
    url(r'^auth/listone/$', auth_views.listone),
]
