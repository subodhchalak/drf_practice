# django imports
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

# in app imports
from watchlist_app.models import (
    Watchlist,
    Platform,
    Review
)

from watchlist_app.generic_serializers import (
    WatchlistSerializer,
    PlatformSerializer,
    ReviewSerializer
)
from watchlist_app.permissons import (
    IsAdminOrReadyOnly,
    IsReviewUserOrReadOnly
)

#---------------------------------------------------------------------------
#                            Watchlist
#---------------------------------------------------------------------------

class WatchlistGListCreateAV(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadyOnly]


class WatchlistGRetriveUpdateDestroyAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


#---------------------------------------------------------------------------
#                            Platform
#---------------------------------------------------------------------------


class PlatformGListCreateAV(generics.ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class PlatformGRetriveUpdateDestroyAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


#---------------------------------------------------------------------------
#                            Review
#---------------------------------------------------------------------------

class ReviewGListAV(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Review.objects.filter(watchlist_id = pk)
        return queryset
    

class ReviewGCreateAV(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def queryset(self, request):
        pk = self.kwargs['pk']
        queryset = Review.objects.all(watchlist_id = pk)
        return queryset

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = Watchlist.objects.get(pk=pk)
        reviewer = self.request.user
        if watchlist.review.filter(reviewer_id = reviewer.id).exists():
            raise ValidationError("Review already exists.")
        else:
            serializer.save(watchlist=watchlist, reviewer=reviewer)


class ReviewGRetriveUpdateDestroyAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    