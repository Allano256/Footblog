
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('nutrition/<str:pk>/',views.nutrition, name='nutrition'),
    
]
