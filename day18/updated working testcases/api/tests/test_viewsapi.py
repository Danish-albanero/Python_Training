from django.test import Client
from rest_framework.test import APITestCase
from api.models import Student
from api.serializers import StudentSerializers






class ApiMethodTest(APITestCase):

    def setUp(self):
        Student.objects.create(name="danish", roll="22", city="lko")
        Student.objects.create(name="Syeddanish", roll="23", city="lucknow")




    def test_postMethod(self):
        c = Client()
        context = {"name": "POSTCHANGES", "roll": "23", "city": "fsdccxz"}
        response = c.post('/studentapi/', context)
        fetch1 = Student.objects.get(name = 'POSTCHANGES')
        serializer = StudentSerializers(fetch1)
        print(serializer.data)

        print(response.status_code, "POST")
        print(response.content)

    def test_method_check(self):
        c = Client()
        # Student.objects.create(name="danish", roll="22", city="lko")
        # Student.objects.create(name="Syeddanish", roll="23", city="lucknow")

        response = c.get('/studentapi/')
        fetch1 = Student.objects.get(name='danish')
        serializer = StudentSerializers(fetch1)
        print(serializer.data)
        print(response.status_code, "GET")





    def test_putMethod(self):
         c = Client()

         path = '/studentapi/1/'
         response = c.put(path, data={'name': 'PutChange','roll':'56','city':'jaipur'}, content_type='application/json', follow=False, secure=False)


         stu = Student.objects.get(id=1)
         serializer = StudentSerializers(stu)


         print(serializer.data)
         print(response.status_code, "PUT")







    def test_patchmethod(self):
         c = Client()
         path = '/studentapi/1/'
         response = c.patch(path, data={'name':'patchChange'}, content_type='application/json', follow=False, secure=False)

         stu = Student.objects.get(id=1)
         serializer = StudentSerializers(stu, partial=True)

         print(serializer.data)
         print(response.status_code, "PATCH")















    def test_deletemethod(self):
          c = Client()
          # Student.objects.create(name="danish", roll="22", city="lko")
          # Student.objects.create(name="Syeddanish", roll="23", city="lucknow")

          response = c.delete('/studentapi/1/')

          print(response.status_code," DELETE")




