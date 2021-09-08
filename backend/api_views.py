from rest_framework import viewsets

from .models import (
    Country,
    Event,
    Medal,
    Participant,
)
from .serializers import (
    CountrySerializer,
    EventSerializer,
    MedalSerializer,
    ParticipantSerializer,
)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()

        date = self.request.query_params.get('date')
        country = self.request.query_params.get('country')

        if date is not None:
            queryset = queryset.filter(event_date=date)

        if country is not None:
            participating_events = Participant.objects.filter(
                country__id=country
            ).values_list('event', flat=True).first()
            queryset = queryset.filter(id=participating_events)

        return queryset


class MedalViewSet(viewsets.ModelViewSet):
    serializer_class = MedalSerializer

    def get_queryset(self):
        queryset = Medal.objects.all()

        event = self.request.query_params.get('event')
        country = self.request.query_params.get('country')

        if event is not None:
            queryset = queryset.filter(event__id=event)

        if country is not None:
            queryset = queryset.filter(country__id=country)

        return queryset


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
