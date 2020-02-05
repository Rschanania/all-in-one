from django.urls import include,path
from exam import views
urlpatterns=[
    path('test',views.test),
    path('Exam',views.exam),
    path('student_mobile',views.mobileDetails),
    path('mobile/',views.StudentMobileNumber.as_view()),
]