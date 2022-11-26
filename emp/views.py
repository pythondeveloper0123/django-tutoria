from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import viewsets

'''
class myapi(viewsets.ModelViewSet):
    try:
        queryset = EmpPersonalDetails.objects.all()
    except EmpPersonalDetails.DoesNotExist:
        Response(data={'msg': 'employee details not found', 'success': 'false',
                 'employee': []}, status=status.HTTP_404_NOT_FOUND)
    serializer_class = EmpPersonalDetailsModelSerializer

'''
# Create your views here.

# does not need pk & id


class EmployeeAPI(APIView):

    def get(self, request):
        try:
            # emp = EmpPersonalDetails.objects.all()  # returns queryset
            emp = Employee.objects.all()  # returns queryset
        # except EmpPersonalDetails.DoesNotExist:
        except Employee.DoesNotExist:
            return Response(data={'msg': 'employee details not found', 'success': 'false', 'employee': []}, status=status.HTTP_404_NOT_FOUND)
        if not emp:
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        # serializer = EmpPersonalDetailsModelSerializer(
        serializer = EmployeeModelSerializer(
            emp, many=True)  # serializes the python data into json
        # send serialized json data to user
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            try:
                # serializer = EmpPersonalDetailsModelSerializer(
                serializer = EmployeeModelSerializer(
                    data=request.data)  # deserialize json data into python data
            except:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'msg': 'employee created successfully', 'success': 'true', 'empid': request.data.get('regid')}, status=status.HTTP_201_CREATED)
            else:
                # if EmpPersonalDetails.objects.filter(email=request.data.get('email')):
                if Employee.objects.filter(email=request.data.get('email')):
                    return Response(data={'msg': 'employe already exist', 'success': 'false'}, status=status.HTTP_200_OK)
                else:
                    return Response(data={'msg': 'invalid body request', 'success': 'false'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(data={'msg': 'employee Creation failed', 'success': 'false'},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#  need pk & id
class EmpAPI(APIView):
    def get_object(self, pk):
        try:
            # emp = EmpPersonalDetails.objects.get(
            emp = Employee.objects.get(
                pk=pk)  # stu.objects.get(id=pk)
        # except EmpPersonalDetails.DoesNotExist:
        except Employee.DoesNotExist:
            return Response(data={'msg': 'no employee found with this regid'}, status=status.HTTP_404_NOT_FOUND)
        return emp

    def get(self, request, pk=None):
        try:
            #     emp = EmpPersonalDetails.objects.get(pk=pk)
            # except EmpPersonalDetails.DoesNotExist:
            emp = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(data={'msg': 'employee details not found', 'success': 'false', 'employee': []}, status=status.HTTP_404_NOT_FOUND)
        # serializer = EmpPersonalDetailsModelSerializer(emp)
        serializer = EmployeeModelSerializer(emp)
        # serializer = EmpPersonalDetailsModelSerializer(self.get_object)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        if pk != '':
            try:
                # emp = EmpPersonalDetails.objects.get(pk=pk)
                emp = Employee.objects.get(pk=pk)
            except:
                return Response(data={'msg': 'no employee found with this regid', 'success': 'false'}, status=status.HTTP_404_NOT_FOUND)
            emp.delete()
            # self.get_object.delete()
            return Response(data={'msg': 'employee deleted successfully', 'success': 'true'},  status=status.HTTP_200_OK)
        else:
            return Response(data={'msg': 'employee deletion failed', 'success': 'false'},  status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        try:
            try:
                # emp = EmpPersonalDetails.objects.get(
                emp = Employee.objects.get(
                    pk=pk)  # stu.objects.get(id=pk)
            # except EmpPersonalDetails.DoesNotExist:
            except Employee.DoesNotExist:
                return Response(data={'msg': 'no employee found with this regid'}, status=status.HTTP_404_NOT_FOUND)
            # for partial update of resource#partial=True
            # serializer = EmpPersonalDetailsModelSerializer(
            serializer = EmployeeModelSerializer(
                data=request.data, instance=emp)
            # serializer = EmpPersonalDetailsModelSerializer(
            #     data=request.data, instance=self.get_object)
            print(serializer)   #
            if serializer.is_valid():
                print(serializer)   #
                serializer.save()
                return Response(data={'msg': 'employee details updated successfully', 'success': 'true'}, status=status.HTTP_200_OK)
            else:
                # if EmpPersonalDetails.objects.filter(email=request.data.get('email')) or EmpPersonalDetails.objects.filter(regid=request.data.get('regid')):
                if Employee.objects.filter(email=request.data.get('email')) or Employee.objects.filter(regid=request.data.get('regid')):
                    return Response(data={'msg': 'employee details updation failed', 'success': 'false'}, status=status.HTTP_200_OK)
                else:
                    return Response(data={'msg': 'invalid body request', 'success': 'false'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(data={'msg': 'employee updation failed', 'success': 'false'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk=None):
        try:
            # emp = EmpPersonalDetails.objects.get(
            emp = Employee.objects.get(
                pk=pk)  # emp.objects.get(id=pk)
        # except EmpPersonalDetails.DoesNotExist:
        except Employee.DoesNotExist:
            return Response(data={'msg': 'Resource Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # serializer = EmpPersonalDetailsModelSerializer(
        serializer = EmployeeModelSerializer(
            data=request.data, instance=emp, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
