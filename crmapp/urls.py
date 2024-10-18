from django.urls import path

from crmapp.views import (
    CRMIndexView,
    KanbanView,
    ReportListView,
    Report001View,
    Report002View,
    Report003View,
    Report004View,
    Report005View,
    NewTaskView,
    TaskView,
    SaveTaskView,
    PersonView,
    PersonListView,
    NewPersonView,
    CustomerView,
    NewCustomerView,
    CustomerListView,
    NewEmployeeView,
    EmployeeView,
    SendToBView,
    SendToCView,
    SendToDView,
    SendToEView,
)

urlpatterns = [    
    path('', CRMIndexView.as_view(), name='show-crm-index'),
     # Отчеты
    path('reports/', ReportListView.as_view(), name='show-reports'),
    path('report_001/', Report001View.as_view(), name='show-report-001'),
    path('report_002/', Report002View.as_view(), name='show-report-002'),
    path('report_003/', Report003View.as_view(), name='show-report-003'),
    path('report_004/', Report004View.as_view(), name='show-report-004'),
    path('report_005/', Report005View.as_view(), name='show-report-005'),
    # Канбан
    path('kanban/', KanbanView.as_view(), name='show-kanban'),
    path('my-kanban/', KanbanView.as_view(), {'onUser': True}, name='show-my-kanban'),
    # Задачи
    path('new-task/<int:customer_id>/', NewTaskView.as_view(), name='new-task'),
    path('task/<int:id>/', TaskView.as_view(), name='show-task'),
    path('save-task/', SaveTaskView.as_view(), name='save-task'),
    # Частные лица
    path('persons/', PersonListView.as_view(), name='persons'),
    path('new-person/', NewPersonView.as_view(), name='new-person'),
    path('person/<int:id>/', PersonView.as_view(), name='show-person'),
    path('save-person/', PersonView.as_view(), name='save-person'),
    # Заказчики
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('new-customer/', NewCustomerView.as_view(), name='new-customer'),
    path('customer/<int:id>/', CustomerView.as_view(), name='show-customer'),
    path('save-customer/', CustomerView.as_view(), name='save-customer'),
    # Сотрудники
    path('new-employee/<int:customer_id>/', NewEmployeeView.as_view(), name='new-employee'),
    path('employee/<int:id>/', EmployeeView.as_view(), name='show-employee'),
    path('save-employee/', EmployeeView.as_view(), name='save-employee'),
    
    path('send-to-b/<int:id>/', SendToBView.as_view(), name='send-to-b'),
    path('send-to-c/<int:id>/', SendToCView.as_view(), name='send-to-c'),
    path('send-to-d/<int:id>/', SendToDView.as_view(), name='send-to-d'),
    path('send-to-e/<int:id>/', SendToEView.as_view(), name='send-to-e'),
]