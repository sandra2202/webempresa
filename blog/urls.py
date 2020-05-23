from django.urls import path
from . import views


urlpatterns = [
    #Paths del blog
        path('', views.blog, name="blog"),
]