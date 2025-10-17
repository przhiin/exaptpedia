from django.shortcuts import render
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework import viewsets


class FeedbackViewSets(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class =  FeedbackSerializer
