from rest_framework import status
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from django.urls import resolve
from api.views import StudentAPI
from rest_framework.status import HTTP_200_OK
import json
from django.urls import reverse, resolve
#from api.models import Student


# class ApiMethodTest(APITestCase):
#
#     def test_method_check(self):
#         url = 'http://127.0.0.1:8000/studentapi/'
#         print(url)
#
#         client = APIClient()
#         #data = {'name': 'Syed MohdDanish'}
#         #data = {'name':'Syed MohdDanish', 'roll':'1', 'city':'lko1'}
#         #response = self.client.generic(method="GET", path='/studentapi/', content_type='application/json')
#
#
#         response = self.client.get(url)
#         #response = self.client.get(url)
#         #self.assertEqual(Student.objects.get().name, 'Syed MohdDanish')
#
#
#
#         #self.assertEqual(response.status_code, status.HTTP_200_OK)
#         print(response.status_code)
#         #print(response.data)
#         print(response)


        #self.assertEquals(response, 200)
        #print(response)
        #response.content


    # def test_postcheck(self):
    #     client = RequestsClient()
    #     context = {"name":"qweqww","roll":"23","city":"fsdccxz"}
    #
    #     response = client.post('http://127.0.0.1:8000/studentapi/', context)
    #     #self.assertEquals(resolve(response).func.view_class, StudentAPI)
    #     print(response.status_code)
    #
    # def test_putcheck(self):
    #     url = reverse('studentbyid')
    #     client = RequestsClient()
    #     con = {'name': 'vcxvcx','roll':22,'city':'jaipur'}
    #     response = client.put(resolve(url), con)
    #     print(response.status_code)
    #
    #     #response = client.post('http://127.0.0.1:8000/studentapi/$/')
    #     #print(response.status_code)
    #
    # def test_patch(self):
    #     #url = 'http://127.0.0.1:8000/studentapi/1/'
    #     #client = RequestsClient()
    #     #content = {"roll":"daxz"}
    #
    #     #response = client.patch(url, content)
    #     #print(response.status_code)
    #     client = RequestsClient()
    #     response = client.patch('http://127.0.0.1:8000/studentapi/<int:pk>/', {'name': 'danish'})
    #
    #     #print(response.status_code)', {'title': 'new idea'}
    #     print(response.status_code)








