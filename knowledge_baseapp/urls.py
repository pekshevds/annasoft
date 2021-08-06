from django.urls import path
from .views import show_knowledge_base_props
from .views import  show_knowledge_base_customers
from .views import show_property
from .views import show_customer
from .views import add_property
from .views import add_record
from .views import show_record

urlpatterns = [    
    path('properties/', show_knowledge_base_props, name='show_knowledge_base_props'),
    path('properties/<int:id>/', show_property, name='show_property'),
    path('properties/add/', add_property, name='add_property'),
    path('customers/', show_knowledge_base_customers, name='show_knowledge_base_customers'),
    path('customers/<int:id>/', show_customer, name='show_customer'),
    path('records/add/', add_record, name='add_record'),
    path('records/<int:id>/', show_record, name='show_record'),
]    