from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ToDoTracker.out.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ToDo/', include('ToDo.urls', namespace='ToDo')),
    url(r'^admin/', include(admin.site.urls)),
]
