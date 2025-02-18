from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('map/', views.map_view, name='map'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/<int:room_number>/', views.room_view, name='room'), 
]
