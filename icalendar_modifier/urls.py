# from django.conf.urls import patterns, include, url

from django.conf.urls import url
from django.contrib import admin

from modifiers import views

# admin.autodiscover()
# import modifiers.views
# urlpatterns = patterns('',
#     url(r'^$', modifiers.views.index, name='index'),
#     url(r'^show$', modifiers.views.show, name='show'),
#     # url(r'^db', hello.views.db, name='db'),
#     # url(r'^admin/', include(admin.site.urls)),
# )

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show$', views.show, name='show'),
    url(r'^admin/', admin.site.urls),
]

