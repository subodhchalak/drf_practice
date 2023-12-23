from django.contrib import admin
from watchlist_app.models import (
    Platform,
    Watchlist
)

# Register your models here.

# @admin.register(Watchlist)
class WatchlistAdmin(admin.TabularInline):
    model = Watchlist
    extra = 0
    can_delete = False


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'created_at',
        'updated_at'
    )
    inlines = (WatchlistAdmin,)

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'platform',
        'is_active', 'created_at', 'updated_at'
    )