from django.urls import path
from secondapp import views
urlpatterns = [
    path('what/',views.what),
]
