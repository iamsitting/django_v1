from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.task_list, name='task_list'),
    url(r'^(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
]
