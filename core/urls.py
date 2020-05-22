from django.urls import path
from . import views


urlpatterns = [
    #Paths del core
        path('', views.home, name="home"),
        path('about/', views.about, name="about"),
        path('services/', views.services, name="services"),
        path('store/', views.services, name="store"),
        path('contact/', views.contact, name="contact"),
        path('blog/', views.blog, name="blog"),
        path('sample/', views.sample, name="sample"),
]