from django.shortcuts import render
from rest_framework import viewsets
from .models import DreamReal
from .serializers import DreamRealSerializer
# Create your views here.


class DreamRealViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DreamReal.objects.all()
    serializer_class = DreamRealSerializer
