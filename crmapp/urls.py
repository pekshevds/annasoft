from django.urls import path

from .views import show_index

from .views import show_persons
from .views import new_person
from .views import save_person
from .views import show_person

from .views import show_customers
from .views import new_customer
from .views import show_customer
from .views import save_customer

from .views import new_employee
from .views import show_employee
from .views import save_employee

from .views import show_canban

from .views import send_to_B
from .views import send_to_C
from .views import send_to_D

from .views import new_task
from .views import save_task
from .views import show_task

urlpatterns = [    
    path('', show_index, name='show-crm-index'),        
    
    # Частные лица
    path('persons/', show_persons, name='persons'),
    path('new-person/', new_person, name='new-person'),
    path('person/<int:id>/', show_person, name='show-person'),
    path('save-person/', save_person, name='save-person'),

    # Заказчики
    path('customers/', show_customers, name='customers'),
    path('new-customer/', new_customer, name='new-customer'),
    path('customer/<int:id>/', show_customer, name='show-customer'),
    path('save-customer/', save_customer, name='save-customer'),

    # Сотрудники
    path('new-employee/<int:customer_id>', new_employee, name='new-employee'),
    path('employee/<int:id>/', show_employee, name='show-employee'),
    path('save-employee/', save_employee, name='save-employee'),
    
    # Задачи
    path('new-task/<int:customer_id>/', new_task, name='new-task'),
    path('task/<int:id>/', show_task, name='show-task'),
    path('save-task/', save_task, name='save-task'),
    
    path('canban/', show_canban, name='show-canban'),
    path('my-canban/', show_canban, {'onUser': True}, name='show-my-canban'),
    
    path('send-to-b/<int:id>/', send_to_B, name='send-to-b'),
    path('send-to-c/<int:id>/', send_to_C, name='send-to-c'),
    path('send-to-d/<int:id>/', send_to_D, name='send-to-d'),
]