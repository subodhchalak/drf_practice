from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny
)

from rest_framework import permissions


class IsAdminOrReadyOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser == True or request.method != 'POST':
            return True 
        return False
    

class IsReviewUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if ( request.user == obj.reviewer) \
            or (
                request.user != obj.reviewer and \
                request.method in permissions.SAFE_METHODS
            ):
            return True
        return False