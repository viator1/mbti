from django.urls import path
from secondapp import views


urlpatterns = [
    path('ISTJ/',views.ISTJ),
    
    path('ISFJ/',views.ISFJ),
    
    path('INFJ/',views.INFJ),
    
    path('INTJ/',views.INTJ),
    
    path('ISTP/',views.ISTP),
    
    path('ISFP/',views.ISFP),
    
    path('INFP/',views.INFP),
    
    path('INTP/',views.INTP),
    
    path('ESTP/',views.ESTP),
    
    path('ESFP/',views.ESFP),
    
    path('ENFP/',views.ENFP),
    
    path('ENTP/',views.ENTP),
    
    path('ESTJ/',views.ESTJ),
    
    path('ESFJ/',views.ESFJ),
    
    path('ENFJ/',views.ENFJ),
    
    path('ENTJ/',views.ENTJ),

    path('ENTJ/',views.ENTJ),

    path('what/',views.what),

    path('kinds/',views.kinds),

    path('freeboard/',views.freeboard),

    path('counseling/',views.counseling),
    
    path('bd/',views.bd),

    path('detail/',views.post_detail)
    
    
    
]
