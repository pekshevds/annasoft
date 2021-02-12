from django.urls import path

from .views import show_index

from .views import show_customer
from .views import save_customer
from .views import show_canban
from .views import send_to_B
from .views import send_to_C
from .views import new_task
from .views import save_task
from .views import show_task

urlpatterns = [    
    path('', show_index, name='show-crm-index'),        
    path('show-customer/<int:id>/', show_customer, name='show-customer'),
    path('save-customer/', save_customer, name='save-customer'),
    path('new-task/<int:customer_id>/', new_task, name='new-task'),
    path('show-task/<int:id>/', show_task, name='show-task'),
    path('save-task/', save_task, name='save-task'),
    path('show-canban/', show_canban, name='show-canban'),
    path('send-to-b/<int:id>/', send_to_B, name='send-to-b'),
    path('send-to-c/<int:id>/', send_to_C, name='send-to-c'),
]