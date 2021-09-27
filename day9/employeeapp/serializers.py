from rest_framework import serializers
from .models import EmployeeDetail

class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = ['name', 'address','pan', 'uan', 'Basic', 'benefits', 'tax']
