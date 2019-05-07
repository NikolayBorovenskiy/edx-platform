from __future__ import absolute_import

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import EntitlementEnrollmentViewSet, EntitlementViewSet

router = DefaultRouter()
router.register(r'entitlements', EntitlementViewSet, base_name='entitlements')

ENROLLMENTS_VIEW = EntitlementEnrollmentViewSet.as_view({
    'post': 'create',
    'delete': 'destroy',
})

app_name = 'v1'
urlpatterns = [
    url(r'', include(router.urls)),
    url(
        r'entitlements/(?P<uuid>{regex})/enrollments$'.format(regex=EntitlementViewSet.ENTITLEMENT_UUID4_REGEX),
        ENROLLMENTS_VIEW,
        name='enrollments'
    )
]
