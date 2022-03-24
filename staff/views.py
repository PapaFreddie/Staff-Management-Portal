from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from staff.models import Departments, Employees
from staff.serializers import DepartmentSerializer, Employees

# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe = False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Added Successfully!!', safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser.parse(request)
        department_serializer = DepartmentSerializer(departments, data = department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Update successful", safe=False)
        return JsonResponse("Failed to update", safe=False)



 