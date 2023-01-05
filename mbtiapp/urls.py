from django.urls import path
from mbtiapp import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    
    path('freeboard/', views.freeboard),
    path('write/', views.write),
    
    
   
]