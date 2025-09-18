from django.contrib import admin
from website.models import Contact

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'updated_date')

admin.site.register(Contact, ModelAdmin)