from django.urls import path
from .views import EmployeeAPI, EmpAPI

urlpatterns = [
    path('employee/', EmployeeAPI.as_view()),
    path('employee/<int:pk>/', EmpAPI.as_view()),
]
