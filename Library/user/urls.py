from django.urls import path
from user import views


urlpatterns=[
    path('login/',views.login),
    path('logout/',views.logout),
    path('profile/',views.profile),
    path('register/',views.register),
]