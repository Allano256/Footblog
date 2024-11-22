
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('nutrition/',views.nutrition, name='nutrition'),
    path('sports_tips/',views.sports_tips, name='sports_tips'),
    path('insights/',views.insights, name='insights'),
    path('health/',views.health, name='health'),
    path('edit/<str:pk>/',views.edit_comment, name='edit'),
    path('delete/<str:pk>/',views.delete_comment, name='delete'),
     
      
]
