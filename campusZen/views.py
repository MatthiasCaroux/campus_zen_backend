from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
