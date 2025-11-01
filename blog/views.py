from django.shortcuts import render
from .models import BlogPost
from .serializers import BlogSerializer
from rest_framework import viewsets


class BlogViewSets(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class =  BlogSerializer
