from django.urls import path
from FN_accounting.views import FNList, FNDetail

urlpatterns = [
    path('fn/', FNList.as_view()),
    path('fn/<str:uid>/', FNDetail.as_view()),
]
