from django.urls import path
from file import views


urlpatterns = [
    path('insert/',views.insert),
    path('show/',views.show),
    path('index/',views.index),
]
