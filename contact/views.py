from rest_framework import viewsets
from .models import contact
from .serializers import contactSerializer

class contactViewSet(viewsets.ModelViewSet):
    queryset = contact.objects.all().order_by('-id')
    serializer_class = contactSerializer
