from django.contrib import admin
from concession.models import SignForm
from .models import details
class SignFormAdmin(admin.ModelAdmin):
    list_display = ('login_id', 'username', 'email', 'password')  # Columns in table format
    list_filter = ('username', 'email')  # Adds filter options in Django Admin
    search_fields = ('username', 'email')  # Adds a search bar
    ordering = ('login_id',)  # Orders records by `login_id`
    actions = ['delete_selected']
admin.site.register(SignForm, SignFormAdmin)  # Registering the model with custom Admin class

class DetailsAdmin(admin.ModelAdmin):
    list_display = ('concession_id', 'studentname', 'collegename', 'station1', 'station2', 'travel_class', 'validity', 'current_date', 'valid_till_date', 'login_id')
    search_fields = ('studentname', 'collegename', 'station1', 'station2')  # Enable search
    list_filter = ('validity', 'travel_class', 'current_date')  # Enable filtering

admin.site.register(details, DetailsAdmin) 