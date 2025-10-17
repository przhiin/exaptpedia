from django.shortcuts import render

# Create your views here.
# community/views.py
from rest_framework import generics, permissions
from .models import Resource
from .serializers import ResourceSerializer

class ResourceListView(generics.ListAPIView):
    queryset = Resource.objects.all().order_by('-uploaded_at')
    serializer_class = ResourceSerializer
    permission_classes = [permissions.AllowAny]  # Public access, change if needed

class ResourceDetailView(generics.RetrieveAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.AllowAny]
