from django.urls import path
from . import views
urlpatterns=[
    path('posts/<int:pk>',views.posts,name="posts pk"),
    path('posts/',views.posts,name="posts"),
]