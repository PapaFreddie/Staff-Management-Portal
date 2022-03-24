from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from staff.models import Departments, Employees
from staff.serializers import DepartmentSerializer, Employees

# Create your views here.
@csrf_exempt
def departmentApi(request)
