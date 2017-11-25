from django.conf.urls import patterns, include, url
from rest_framework import routers

from accounts.api import AccountViewSet
from tags.api import TagViewSet
from mode.api import ModeViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'tag', TagViewSet)
router.register(r'mode', ModeViewSet)

urlpatterns = patterns(
    'api',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
