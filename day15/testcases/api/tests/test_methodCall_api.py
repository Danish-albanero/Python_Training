
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
from django.urls import resolve
from api.views import StudentAPI




class ApiMethodTest(APITestCase):

    def test_method_check(self):

        client = RequestsClient()


        response = client.get('http://127.0.0.1:8000/studentapi/')
        #self.assertEquals(response, 200)
        response.content


    def test_postcheck(self):
        client = RequestsClient()
        context = {"name":"qweqww","roll":"23","city":"fsdccxz"}

        response = client.post('http://127.0.0.1:8000/studentapi/', context)
        #self.assertEquals(resolve(response).func.view_class, StudentAPI)
        print(response.status_code)

    def test_putcheck(self):
        client = RequestsClient()

        response = client.post('http://127.0.0.1:8000/studentapi/$/')
        print(response.status_code)

    def test_patch(self):
        client = RequestsClient()
        content = {"roll":"daxz"}

        response = client.post('http://127.0.0.1:8000/studentapi/2/', content)
        response.status_code






