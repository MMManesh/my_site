from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'status', 'counted_views')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content', 'author')
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'updated_date', 'counted_views')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'status', 'publication_date')
        }),
        ('Timestamps', {
            'fields': ('created_date', 'updated_date', 'counted_views'),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Post, PostAdmin)