from django.test import SimpleTestCase
from django.urls import reverse,resolve
from api.views import StudentAPI




class ApiUrlsTests(SimpleTestCase):
    def test_get_student(self):
        url = reverse('studentapi')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func.view_class, StudentAPI)



