from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MembersViewSets, JobCategoryViewSet

router = DefaultRouter()
router.register(r'members', MembersViewSets)
router.register(r'job-categories', JobCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
