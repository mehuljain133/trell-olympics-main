from rest_framework import routers
from backend import api_views


router = routers.DefaultRouter()
router.register(r'countries', api_views.CountryViewSet, basename='countries')
router.register(r'events', api_views.EventViewSet, basename='events')
router.register(r'medals', api_views.MedalViewSet, basename='medals')
router.register(r'participants', api_views.ParticipantViewSet,
                basename='participants')
