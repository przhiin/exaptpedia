from django.shortcuts import render
from .models import Events
from .serializers import EventSerializer
from rest_framework import viewsets


class EventViewSets(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class =  EventSerializer
