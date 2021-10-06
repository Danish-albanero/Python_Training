from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import logging
# Create your views here.


logger = logging.getLogger()

# Create your views here.


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            logger.info(Response(serializer.data))
            return Response(serializer.data)
        stu = Student.objects.all()
        print(stu)
        serializer = StudentSerializers(stu, many=True)
        print(serializer.data)
        logger.info(Response(serializer.data))
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED))
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        
        logger.warning(Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST))
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(Response({'msg':'Data Upated'}))
            return Response({'msg':'Data Upated'})
        logger.warning(Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(Response({'msg':'Data Upated'}))
            return Response({'msg':'Data Upated'})
        logger.info(Response(serializer.errors))
        return Response(serializer.errors)

    def delete(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        logger.info(Response({'msg':'Data Deleted'}))
        return Response({'msg':'Data Deleted'})















