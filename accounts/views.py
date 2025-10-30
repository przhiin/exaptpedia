from rest_framework import viewsets, filters
from .models import Members
from .serializers import MembersSerializer

class MembersViewSets(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

    # Allow both search and ordering via filters
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'phone', 'email', 'position']
    ordering_fields = ['name', 'email', 'phone', 'occupation', 'id']
    ordering = ['id']

    def get_queryset(self):
        queryset = Members.objects.all()
        sort_param = self.request.query_params.get('sort', None)

        if sort_param == 'name_asc':
            queryset = queryset.order_by('name')       # ascending
        elif sort_param == 'name_desc':
            queryset = queryset.order_by('-name')      # descending

        return queryset


    def list(self, request, *args, **kwargs):
        print("Hello from MembersViewSets")
        return super().list(request, *args, **kwargs)
