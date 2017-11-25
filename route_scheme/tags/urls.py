from django.conf.urls import patterns, include, url
from rest_framework import routers

from tags.api import TagViewSet

router = routers.DefaultRouter()
router.register(r'tag', TagViewSet)
# router.register(r'mode', ModeViewSet)

urlpatterns = patterns(
    url(r'^', include(router.urls)),
)
