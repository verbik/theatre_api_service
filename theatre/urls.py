from django.urls import path, include
from rest_framework import routers

from .views import (
    GenreViewSet,
    ActorViewSet,
    PlayViewSet,
    PerformanceViewSet,
    TheatreHallViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatre_halls", TheatreHallViewSet)
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
