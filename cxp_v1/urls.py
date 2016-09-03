from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.foo, name='foo'),
    url(r'^dataplot$', views.dataplot, name='dataplot'),
    url(r'^datasync$', views.datasync, name='datasync'),
#    url(r'^line_chart/$', views.line_chart, name='line_chart'),
#    url(r'^line_chart/json/$', views.line_chart_json, name='line_chart_json'),
]
