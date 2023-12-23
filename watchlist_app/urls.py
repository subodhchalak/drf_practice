from django.urls import path
from watchlist_app.views import (
    watchlist_list,
    watchlist_details
)

from watchlist_app.api_views import (
    WatchlistAV,
    PlatformAV
)

# urlpatterns = [
#     path('list/', Watchlist_list, name='Watchlist_list'),
#     path('details/<int:pk>/', Watchlist_details, name='Watchlist_details')
# ]


urlpatterns = [
    path('watchlist/', WatchlistAV.as_view(), name='watchlist'),
    path('platform/', PlatformAV.as_view(), name='platform')
]