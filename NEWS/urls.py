from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSets, AnnouncementViewSets

router = DefaultRouter()
router.register(r'News', NewsViewSets)
router.register(r'Announcement', AnnouncementViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
