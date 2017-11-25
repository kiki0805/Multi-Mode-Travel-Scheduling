from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'route_scheme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include('route_scheme.api_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^scheme/$', 'scheme.views.scheme'),
]
