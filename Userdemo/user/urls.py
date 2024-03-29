from django.urls import path
from .views import (RegisterView,
    MyObtainTokenPairView,
    Updatewid,
    Updateuid,
    Getuid,
    Getwid,
    GetNameView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    path('update-wid/', Updatewid.as_view()),
    path('update-uid/', Updateuid.as_view()),
    path('get-wid/', Getwid.as_view()),
    path('get-uid/', Getuid.as_view()),
    path('get-name/', GetNameView.as_view()),
]