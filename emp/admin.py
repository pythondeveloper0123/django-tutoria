from django.contrib import admin
from .models import EmpPhoto, EmpQualification, EmpWorkExperience, EmpAddressDetails, EmpPersonalDetails, EmpProjects, EmployeeQualification, EmployeeWorkExperience, EmployeeAddress, Employee, EmployeeProjects

# Register your models here.

'''
@admin.register(EmpPersonalDetails)
class EmpPersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ('regid', 'name', 'email', 'age', 'gender', 'phoneNo',)


@admin.register(EmpAddressDetails)
class EmpAddressDetailsAdmin(admin.ModelAdmin):
    list_display = ('emp', 'hno', 'street', 'city', 'state', )


@admin.register(EmpWorkExperience)
class EmpWorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('emp', 'companyName', 'fromDate', 'toDate', 'address', )


@admin.register(EmpQualification)
class EmpQualificationAdmin(admin.ModelAdmin):
    list_display = ('emp', 'qualificationName', 'percentage', )


@admin.register(EmpProjects)
class EmpProjectsAdmin(admin.ModelAdmin):
    list_display = ('emp', 'title', 'description', )


@admin.register(EmpPhoto)
class EmpPhotoAdmin(admin.ModelAdmin):
    list_display = ('emp', 'photo')

'''


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('regid', 'name', 'email', 'age', 'gender', 'phoneNo',)


@admin.register(EmployeeAddress)
class EmployeeAddressDetailsAdmin(admin.ModelAdmin):
    list_display = ('emp', 'hno', 'street', 'city', 'state', )


@admin.register(EmployeeWorkExperience)
class EmployeeWorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('emp', 'companyName', 'fromDate', 'toDate', 'address', )


@admin.register(EmployeeQualification)
class EmployeeQualificationAdmin(admin.ModelAdmin):
    list_display = ('emp', 'qualificationName', 'percentage', )


@admin.register(EmployeeProjects)
class EmployeeProjectsAdmin(admin.ModelAdmin):
    list_display = ('emp', 'title', 'description', )
