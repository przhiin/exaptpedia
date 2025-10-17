from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSets

router = DefaultRouter()
router.register(r'Feedback', FeedbackViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
