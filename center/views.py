from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from .serializer import CenterSerializer
from .models import Center
from .permissions import permissionsClass

class CenterListView(ListAPIView, CreateAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
    permission_classes = (permissionsClass,IsAuthenticated,)

class CenterDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer
    permission_classes = (permissionsClass,IsAuthenticated, )
