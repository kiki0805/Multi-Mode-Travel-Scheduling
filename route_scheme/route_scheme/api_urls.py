from django.conf.urls import patterns, include, url
from rest_framework import routers

from accounts.api import AccountViewSet
from tags.api import TagViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'tag', TagViewSet)
# route.register(r'mode', ModeViewSet)

urlpatterns = patterns(
    'api',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
