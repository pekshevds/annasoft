from django.urls import path

from authapp.views import (
    LoginView,
    LogoutView
)

app_name = 'authapp'

urlpatterns = [    
    path('', LoginView.as_view(), name='show-auth'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]