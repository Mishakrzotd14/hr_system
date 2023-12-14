from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
