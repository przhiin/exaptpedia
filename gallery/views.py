from django.shortcuts import render
from .models import Gallery
from .serializers import GallerySerializer
from rest_framework import viewsets


class GalleryViewSets(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class =  GallerySerializer
