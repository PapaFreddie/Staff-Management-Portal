from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from staff.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    model = Departments
    fields = ('DepartmentId', 'DepartmentName')


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')