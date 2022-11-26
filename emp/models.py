from django.db import models
# Create your models here.


# class EmpPersonalDetails(models.Model):
class Employee(models.Model):
    regid = models.AutoField(primary_key=True)
    # regid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='empphoto', null=True, blank=True)

    def __str__(self):
        return f'{self.regid}'


# class EmpAddressDetails(models.Model):
class EmployeeAddress(models.Model):
    # emp = models.OneToOneField(
    #     EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmpAddressDetails')
    emp = models.OneToOneField(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeAddress')
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.emp.regid}'
# 100322451807


# class EmployeeWorkExperience(models.Model):
class EmployeeWorkExperience(models.Model):
    # emp = models.ForeignKey(EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmpWorkExperience')
    emp = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeWorkExperience')
    companyName = models.CharField(max_length=100,  null=True, blank=True)
    fromDate = models.CharField(max_length=100, null=True, blank=True)
    toDate = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.emp.regid}'


# class EmpQualification(models.Model):
class EmployeeQualification(models.Model):
    # emp = models.ForeignKey(
    #     EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmployeeQualification')
    emp = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmpQualification')
    qualificationName = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.emp.regid}'


# class EmpProjects(models.Model):
class EmployeeProjects(models.Model):
    # emp = models.ForeignKey(
    #     EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmpProjects')
    emp = models.ForeignKey(
        Employee, on_delete=models.CASCADE,  related_name='EmployeeProjects')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.emp.regid}'


# class EmpPhoto(models.Model):
#     emp = models.OneToOneField(
#         EmpPersonalDetails, on_delete=models.CASCADE,  related_name='EmpPhoto')
#     photo = models.ImageField(upload_to='empphoto',
#                               default='', null=True, blank=True)

#     def __str__(self):
#         return f'{self.emp.regid}'

# pip install drf-writable-nested
# pip install drf-extra-fields
