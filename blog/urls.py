from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSets

router = DefaultRouter()
router.register(r'Blog', BlogViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
