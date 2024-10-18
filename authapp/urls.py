from django.urls import path

from .views import show_auth
from .views import set_login
from .views import set_logout

app_name = 'authapp'

urlpatterns = [    
    path('', show_auth, name='show-auth'),
    path('login/', set_login, name='login'),
    path('logout/', set_logout, name='logout'),
]