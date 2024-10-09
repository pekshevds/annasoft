from django.urls import path
from .views import fn_list

urlpatterns = [
    path('list/', fn_list, name='fn_list'),
]