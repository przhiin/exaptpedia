from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AchievementViewSets

router = DefaultRouter()
router.register(r'Achievement', AchievementViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
