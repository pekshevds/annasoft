from django.urls import path
from FN_accounting.views import FNList, FNDetail, Point_of_saleList
from FN_accounting.views import KKTDetail, KKTFilterByPointOfSalesList

urlpatterns = [
    path('fn/kkt/list/<str:uid>/', KKTFilterByPointOfSalesList.as_view()),
    path('fn/', FNList.as_view()),
    path('fn/<str:uid>/', FNDetail.as_view()),
    path('fn/get-pos-list/<str:pk>/', Point_of_saleList.as_view()),
    path('fn/kkt/<str:uid>/', KKTDetail.as_view()),
]
