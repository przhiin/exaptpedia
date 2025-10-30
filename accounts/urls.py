from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MembersViewSets

router = DefaultRouter()
router.register(r'Members', MembersViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
