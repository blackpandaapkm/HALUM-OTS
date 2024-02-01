from django.urls import path
from .views import *
urlpatterns=[   
    path('',index,name='home'),
    path('reg/', reg, name='reg'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
]
