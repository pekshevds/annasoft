from django.urls import path

from .views import show_index

from .views import show_customer
from .views import save_customer

urlpatterns = [    
    path('', show_index, name='show-crm-index'),        
    path('show-customer/<int:id>/', show_customer, name='show-customer'),
    path('save-customer/', save_customer, name='save-customer'),
]