from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSets

router = DefaultRouter()
router.register(r'Event', EventViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
