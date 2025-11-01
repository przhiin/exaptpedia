from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Members, JobCategory
from .serializers import MembersSerializer, JobCategorySerializer

class MembersViewSets(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'phone', 'email', 'position']
    ordering_fields = ['name', 'email', 'phone', 'occupation_category', 'id']
    ordering = ['id']
    filterset_fields = ['occupation_category']

    def get_queryset(self):
        queryset = Members.objects.all()
        
        # Handle sorting
        sort_param = self.request.query_params.get('sort', None)
        if sort_param == 'name_asc':
            queryset = queryset.order_by('name')
        elif sort_param == 'name_desc':
            queryset = queryset.order_by('-name')
        
        # Handle category filtering
        category_id = self.request.query_params.get('category_id', None)
        category_name = self.request.query_params.get('category', None)
        
        if category_id:
            queryset = queryset.filter(occupation_category__id=category_id)
        elif category_name:
            queryset = queryset.filter(occupation_category__name__iexact=category_name)
        
        return queryset

class JobCategoryViewSet(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all().order_by('name')
    serializer_class = JobCategorySerializer