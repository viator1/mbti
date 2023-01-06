from django.urls import path
from mbtiapp import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    
    path('freeboard/', views.freeboard),
    path('write/', views.write),
    path('freeboard/detail/<int:id>/', views.detail),
    path('freeboard/edit/<int:id>/', views.edit),
    path('freeboard/delete/<int:id>/', views.delete),
    path('freeboard/comment/', views.comment),
    
    
   
]