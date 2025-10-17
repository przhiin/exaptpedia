from django.shortcuts import render
from .models import News, Announcement
from .serializers import NewsSerializer, AnnouncementSerializer
from rest_framework import viewsets


class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    Serializer_class =  NewsSerializer



class AnnouncementViewSets(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    Serializer_class =  AnnouncementSerializer