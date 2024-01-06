# django imports
from django.urls import path

# rest_framework imports
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

# in app imports
from user_app.views import (
    UserRegistrationMV,
    UserLogoutMV
)

router = routers.SimpleRouter()
router.register('register', UserRegistrationMV, basename='register')
router.register('logout', UserLogoutMV, basename='logout')

urlpatterns = [
    path('login/', obtain_auth_token, name='login')
]

urlpatterns += router.urls