from django.contrib import admin
from watchlist_app.models import (
    Movie
)

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'is_active', 'created_at', 'updated_at'
    )