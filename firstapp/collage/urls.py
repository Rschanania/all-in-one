from django.urls import path,include
from . import views
#from django.views.generic import TemplateView
from . import views


urlpatterns=[

    #path('cbview/',TemplateView.as_view(template_name='collage/collage_view.html')),
    #with the help of defined class cbview
    path('cbview/',views.cbview.as_view()),


]