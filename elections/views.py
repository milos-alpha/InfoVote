# views.py
from django.views.generic import ListView
from django.db.models import Q
from django.db.models.functions import ExtractYear
from .models import Election

class PastElectionsView(ListView):
    model = Election
    template_name = 'elections.html'
    context_object_name = 'elections'
    paginate_by = 20  # Add pagination for better performance

    def get_queryset(self):
        queryset = Election.objects.filter(status='COMPLETED').order_by('-start_date')
        
        # Get search parameters from GET request
        search_query = self.request.GET.get('search', '')
        election_type = self.request.GET.get('type', '')
        year = self.request.GET.get('year', '')
        
        # Apply filters based on search parameters
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(location__icontains=search_query) 
            )
        
        if election_type:
            queryset = queryset.filter(election_type=election_type)
            
        if year:
            queryset = queryset.filter(start_date__year=year)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add search parameters to context for form persistence
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_type'] = self.request.GET.get('type', '')
        context['selected_year'] = self.request.GET.get('year', '')
        
        # Add filter options to context
        context['election_types'] = Election.ELECTION_TYPES
        context['available_years'] = Election.objects.filter(
            status='COMPLETED'
        ).annotate(
            year=ExtractYear('start_date')
        ).values_list('year', flat=True).distinct().order_by('-year')
        
        # Add total results count
        context['total_results'] = self.get_queryset().count()
        
        return context
