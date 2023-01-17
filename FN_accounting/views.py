from django.shortcuts import render
from baseapp.core import get_context
from rest_framework import generics, permissions

from .models import FN
from .serializers import FNSerializer

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
        return render(request, 'FN_accounting/fn_list.html', context)