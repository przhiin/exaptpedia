from django.shortcuts import render
from .models import Achievement
from .serializers import AchievementSerializer
from rest_framework import viewsets


class AchievementViewSets(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class =  AchievementSerializer
