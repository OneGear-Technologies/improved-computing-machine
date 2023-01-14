from django.contrib import admin
from django.urls import path,include
from .views import ProfileView, PollStat, LockStat,UnlockStat


urlpatterns = [
    path('',ProfileView.as_view(), name="Listview"),
    path('get-stat/',PollStat.as_view(), name="GetStat"),
    path('lock/', LockStat.as_view(), name="Lock"),
    path('unlock/', UnlockStat.as_view(), name="Unlock")
]
