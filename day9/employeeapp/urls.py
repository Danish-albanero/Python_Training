
from django.urls import path
from .views import employee_list,employee_detail,employee_above,taxUp,empTaxUpdate

urlpatterns = [
    path('employee/', employee_list),
    path('empdetail/<int:pk>/', employee_detail),
    path('empl/', employee_above),
    path('tax/', taxUp),
    path('taxup/', empTaxUpdate),



]
