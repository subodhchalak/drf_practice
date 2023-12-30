from django.urls import path
from rest_framework import routers

from watchlist_app.views import (
    watchlist_list,
    watchlist_details
)

from watchlist_app.api_views import (
    WatchlistAV,
    PlatformAV
)

from watchlist_app.generic_views import (
    WatchlistGListCreateAV,
    WatchlistGRetriveUpdateDestroyAV,
    PlatformGListCreateAV,
    PlatformGRetriveUpdateDestroyAV,
    ReviewGListAV,
    ReviewGCreateAV,
    ReviewGRetriveUpdateDestroyAV
)

from watchlist_app.viewsets_views import (
    WatchlistVS,
    PlatformMV
)

# urlpatterns = [
#     path('list/', Watchlist_list, name='Watchlist_list'),
#     path('details/<int:pk>/', Watchlist_details, name='Watchlist_details')
# ]


# urlpatterns = [
#     path('watchlist/', WatchlistAV.as_view(), name='watchlist'),
#     path('platform/', PlatformAV.as_view(), name='platform')
# ]


router = routers.SimpleRouter()
router.register(r'watchlist', WatchlistVS, basename='watchlist')
router.register(r'platform', PlatformMV, basename='platform')


urlpatterns = [

    #--------------------------------- Watchlist -------------------------------
    
    path(
        route = 'watchlist/',
        view = WatchlistGListCreateAV.as_view(),
        name = 'watchlist'
    ),
    path(
        route = 'watchlist/<int:pk>/',
        view = WatchlistGRetriveUpdateDestroyAV.as_view(), 
        name = 'watchlist_detail'
    ),

    #--------------------------------- Platform --------------------------------
    
    # path(
    #     route = 'platform/',
    #     view = PlatformGListCreateAV.as_view(),
    #     name= 'platform'
    # ),
    # path(
    #     route = 'platform/<int:pk>/',
    #     view = PlatformGRetriveUpdateDestroyAV.as_view(), 
    #     name = 'platform_detail'
    # ),

    #--------------------------------- Review ----------------------------------
    
    path(
        route = 'watchlist/<int:pk>/review/',
        view = ReviewGListAV.as_view(),
        name= 'review'
    ),
    path(
        route = 'watchlist/<int:pk>/review_create/',
        view = ReviewGCreateAV.as_view(),
        name = 'review_create'
    ),
    path(
        route = 'watchlist/review/<int:pk>/',
        view = ReviewGRetriveUpdateDestroyAV.as_view(), 
        name = 'review_detail'
    )
]


# urlpatterns += router.urls