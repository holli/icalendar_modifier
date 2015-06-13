from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import modifiers.views

urlpatterns = patterns('',
    url(r'^$', modifiers.views.index, name='index'),
    url(r'^show$', modifiers.views.show, name='show'),
    # url(r'^db', hello.views.db, name='db'),
    # url(r'^admin/', include(admin.site.urls)),
)
