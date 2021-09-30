from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
#from rest_framework.permissions import IsAdminUser
# Create your views here.
class StudentModelViewsSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #authentication_classes = [BaseAuthentication]
    #permission_classes = [IsAdminUser]

