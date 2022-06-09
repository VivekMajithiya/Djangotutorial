from django.contrib import admin

# Register your models here.
from moviesapi.models import Movies

# admin.site.register(Movies)

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'released']
    list_display = ['title','released']
    list_filter = ['released','is_released']
    search_fields = ['title']