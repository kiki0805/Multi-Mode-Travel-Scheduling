from django.conf.urls import patterns, include, url
from rest_framework import routers

from accounts.api import AccountViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
# router.register(r'mode', ModeViewSet)

urlpatterns = patterns(
    url(r'^', include(router.urls)),
)
