from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.foo, name='foo'),
    url(r'^login$', views.login, name='login'),
    url(r'^datasync$', views.datasync, name='datasync'),
]
