from django.contrib import admin
from watchlist_app.models import (
    Platform,
    Watchlist,
    Review
)

# Register your models here.

#--------------------------- WatchlistTabularInline ----------------------------


# @admin.register(Watchlist)
class WatchlistTabularInline(admin.TabularInline):
    model = Watchlist
    extra = 0
    can_delete = False


#-------------------------------- PlatformAdmin --------------------------------


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'created_at',
        'updated_at'
    )
    inlines = (WatchlistTabularInline, )


#------------------------------- WatchlistAdmin --------------------------------


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'platform',
        'is_active', 'created_at', 'updated_at'
    )


#-------------------------------- ReviewAdmin ----------------------------------


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'reviewer', 'watchlist', 'description',
        'is_active', 'created_at', 'updated_at'
    )