from rest_framework import viewsets, mixins, status
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from .models import (
    Genre,
    Actor,
    TheatreHall,
    Play,
    Performance,
)

from .serializers import (
    GenreSerializer,
    ActorSerializer,
    TheatreHallSerializer,
    PlaySerializer,
    PerformanceSerializer,
    TicketSerializer,
    ReservationSerializer,
)


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class TheatreHallViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PlayViewSet(
    ReadOnlyModelViewSet,
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = Play.objects.prefetch_related("genres", "actors")
    serializer_class = PlaySerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = (
        Performance.objects.all()
        .select_related("play", "theatre_hall")
    )
    serializer_class = PerformanceSerializer
