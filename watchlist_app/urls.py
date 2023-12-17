from django.urls import path
from watchlist_app.views import (
    movie_list,
    movie_details
)

from watchlist_app.api_views import (
    MovieListAV,

)

# urlpatterns = [
#     path('list/', movie_list, name='movie_list'),
#     path('details/<int:pk>/', movie_details, name='movie_details')
# ]


urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie_list')
]