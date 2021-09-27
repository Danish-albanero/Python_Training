from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import EmployeeDetail
from .serializers import EmployeeDetailSerializer
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        emp = EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(emp, many=True)
        for item in serializer.data:
            if item['tax'] == '10':
                print(item)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeDetailSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def employee_detail(request, pk):
    try:
        em = EmployeeDetail.objects.get(pk=pk)
    except EmployeeDetail.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = EmployeeDetailSerializer(em)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeDetailSerializer(em, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        em.delete()
        return HttpResponse(status=204)
@csrf_exempt
def employee_above(request):
    if request.method == 'GET':
        emp = EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(emp, many=True)
        for item in serializer.data:
            if item['Basic'] > '2000':
                item['Basic'] = '6000'
                item1 = item

                print(item)
        return JsonResponse(item1, safe=False)
@csrf_exempt
def taxUp(request):
    if request.method == 'GET':
        EmployeeDetail.objects.filter(tax=10).update(tax=15)
        emp = EmployeeDetail.objects.all()

        serializer = EmployeeDetailSerializer(emp, many=True)



        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def empTaxUpdate(request):
    if request.method == 'GET':
        emp = EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(emp, many=True)
        for item in serializer.data:
            pay =item['Basic']
            t= item['tax']
            pay = int(pay) - int(t)/100
        EmployeeDetail.objects.filter(tax=15).update(Basic = pay)
        emp = EmployeeDetail.objects.all()

        serializer = EmployeeDetailSerializer(emp, many=True)
        return JsonResponse(serializer.data, safe=False)














