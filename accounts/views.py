from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets


class CustomUserViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class =  CustomUserSerializer

    def list(self, request, *args, **kwargs):
        print("Hello from Chaandi kuttan")
        return super().list(request, *args, **kwargs)