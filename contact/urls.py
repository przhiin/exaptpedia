from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import contactViewSet

router = DefaultRouter()
router.register(r'contact', contactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
