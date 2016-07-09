from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.foo, name='foo'),
    url(r'^dataplot$', views.dataplot, name='dataplot'),
    url(r'^datasync$', views.datasync, name='datasync'),
]
