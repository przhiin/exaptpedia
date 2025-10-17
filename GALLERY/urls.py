from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryViewSets

router = DefaultRouter()
router.register(r'Gallery', GalleryViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
