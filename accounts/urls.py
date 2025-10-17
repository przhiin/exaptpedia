from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSets

router = DefaultRouter()
router.register(r'customUser', CustomUserViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
