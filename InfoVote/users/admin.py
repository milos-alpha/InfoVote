from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Voter
from elections.models import ElectionRequirement, Election, CarouselImage

admin.site.site_header = 'Elections Administration'
admin.site.site_title = 'Elections Admin Portal'
admin.site.index_title = 'Welcome to Elections Admin Portal'

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'full_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Election)
admin.site.register(Voter)
admin.site.register(CarouselImage)
@admin.register(ElectionRequirement)
class ElectionRequirementAdmin(admin.ModelAdmin):
    # List display shows these fields in the list view
    list_display = ['id', 'name', 'created_at', 'updated_at']  
    
    # Add search functionality
    search_fields = ['name', 'description']  
    
    # Add filters in the right sidebar
    list_filter = ['created_at', 'updated_at']  
    
    # Organize fields in the edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')  
        }),
        ('Additional Information', {
            'fields': ('is_mandatory', 'min_age', 'document_needed'),  
            'classes': ('collapse',)
        }),
    )
    
    # Make fields readonly if needed
    readonly_fields = ['created_at', 'updated_at']  
    
    # Number of items per page
    list_per_page = 20

    actions = ['custom_action']  # add custom actions if needed

    def custom_action(self, request, queryset):
        # Add custom bulk actions here
        pass
    custom_action.short_description = "Custom action description"