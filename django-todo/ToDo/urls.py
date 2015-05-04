__author__ = 'juancabello'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^add/$', views.add, name='add'),
    url(r'^about/$', views.about, name='about'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
]