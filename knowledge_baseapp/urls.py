from django.urls import path

from knowledge_baseapp.views import (
    RecordsListView,
    RecordView,
    AddRecordView,
    SaveRecordView
)

urlpatterns = [    
    path('records/add/', AddRecordView.as_view(), name='add_record'),
    path('records/save/<int:id>/', SaveRecordView.as_view(), name='save_record'),
    path('records/<int:id>/', RecordView.as_view(), name='show_record'),
    path('records/', RecordsListView.as_view(), name='show_all_records'),
]    