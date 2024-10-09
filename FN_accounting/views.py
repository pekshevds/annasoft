from django.shortcuts import render
from baseapp.core import get_context
from rest_framework import generics, permissions

from .models import FN, KKT, Point_of_sale
from .serializers import FNSerializer, Point_of_saleSerializer, KKTFullSerializer
import json

class KKTFilterByPointOfSalesList(generics.ListAPIView):
    serializer_class = KKTFullSerializer
    def get_queryset(self):
        pos_uid = self.kwargs['uid']
        return KKT.objects.filter(point_of_sale__uid=pos_uid)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class KKTDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KKT.objects.all()
    serializer_class = KKTFullSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'uid'

class Point_of_saleList(generics.ListCreateAPIView):
    serializer_class = Point_of_saleSerializer
    def get_queryset(self):
        customer_pk = self.kwargs['pk']
        return Point_of_sale.objects.filter(customer__pk=customer_pk)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FNList(generics.ListCreateAPIView):
    queryset = FN.objects.all()
    serializer_class = FNSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FNDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FN.objects.all()
    serializer_class = FNSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'uid'

def fn_list(request):
    context = get_context()
    if request.user.is_authenticated:
        customer_unic_list = []
        customer_list = []
        for item in KKT.objects.all():
            if item.customer.name not in customer_unic_list:
                customer_unic_list.append(item.customer.name)
                customer_list.append({
                    "name": item.customer.name,
                    "inn":item.customer.inn,
                    "pk":item.customer.pk,
                    "isActive": False,
                })   
        context.update({
            "customer_list": json.dumps(customer_list),
        })
        return render(request, 'FN_accounting/fn_list.html', context)