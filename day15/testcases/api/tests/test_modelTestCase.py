from django.test import TestCase
from api.models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name = "danish",roll = "22", city= "lko")
        Student.objects.create(name="Syeddanish", roll="23", city="lucknow")

    def test_student_city(self):
        a = Student.objects.get(name = "danish")
        b = Student.objects.get(name = "Syeddanish")
        self.assertEquals(a.name , 'danish')
        self.assertEquals(b.name, 'Syeddanish')