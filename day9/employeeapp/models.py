from djongo import models
# Create your models here.
class EmployeeDetail(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    pan = models.CharField(max_length=30)
    uan = models.CharField(max_length=30)
    Basic = models.CharField(max_length=30)
    benefits = models.CharField(max_length=30)
    tax = models.CharField(max_length=30)





    def __str__(self):
        return self.name










