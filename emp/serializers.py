from rest_framework import serializers
from .models import EmpQualification, EmpWorkExperience, EmpProjects, EmpPersonalDetails, EmpAddressDetails, EmpPhoto, EmployeeAddress, EmployeeWorkExperience, EmployeeQualification, EmployeeProjects, Employee
from drf_writable_nested import WritableNestedModelSerializer
from drf_extra_fields.fields import Base64ImageField


# class EmpAddressDetailsModelSerializer(serializers.ModelSerializer):
class EmployeeAddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        # model = EmpAddressDetails
        model = EmployeeAddress
        fields = ('hno',)  # 'street', 'city', 'state',

    # def create(self, validated_data):
        # return EmpAddressDetails.objects.create(**validated_data)


# class EmpWorkExperienceModelSerializer(serializers.ModelSerializer):
class EmployeeWorkExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        # model = EmpWorkExperience
        model = EmployeeWorkExperience
        fields = ('companyName',)  # 'fromDate', 'toDate', 'address',

    def create(self, validated_data):
        # return EmpWorkExperience.objects.create(**validated_data)
        return EmployeeWorkExperience.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # return EmpWorkExperience.update(instance, **validated_data)
        return EmployeeWorkExperience.update(instance, **validated_data)


# class EmpQualificationModelSerializer(serializers.ModelSerializer):
class EmployeeQualificationModelSerializer(serializers.ModelSerializer):
    class Meta:
        # model = EmpQualification
        model = EmployeeQualification
        fields = ('qualificationName', 'percentage', )

    # def create(self, validated_data):
        # return EmpQualification.objects.create(**validated_data)


# class EmpProjectsModelSerializer(serializers.ModelSerializer):
class EmployeeProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        # model = EmpProjects
        model = EmployeeProjects
        fields = ('title', 'description', )

    # def create(self, validated_data):
        # return EmpProjects.objects.create(**validated_data)


class EmpPhotoModelSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = EmpPhoto
        fields = ('photo',)

    def create(self, validated_data):
        photo = self.validated_data.pop('photo')
        # return EmpPhoto.objects.create(**validated_data)
        return EmpPhoto.objects.create(photo=photo)


# class EmpPersonalDetailsModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
class EmployeeModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    # EmpAddressDetails = EmpAddressDetailsModelSerializer()
    # EmpWorkExperience = EmpWorkExperienceModelSerializer(many=True)
    # EmpQualification = EmpQualificationModelSerializer(many=True)
    # EmpProjects = EmpProjectsModelSerializer(many=True)
    # EmpPhoto = EmpPhotoModelSerializer()

    EmployeeAddress = EmployeeAddressModelSerializer()
    EmployeeWorkExp = EmployeeWorkExperienceModelSerializer(many=True)
    EmployeeQualification = EmployeeQualificationModelSerializer(many=True)
    EmployeeProjects = EmployeeProjectsModelSerializer(many=True)

    class Meta:
        # model = EmpPersonalDetails
        model = Employee

        # fields = ('regid', 'name', 'email', 'age',
        #           'gender', 'phoneNo', 'EmpWorkExperience',   'photo',)  # 'EmpAddressDetails',  'EmpQualification', 'EmpProjects',

        fields = ('regid', 'name', 'email', 'age',
                  'gender', 'phoneNo', 'EmployeeAddress', 'EmployeeWorkExperience',   'photo', 'EmployeeAddress',  'EmployeeQualification', 'EmployeeProjects',)

    # def create(self, validated_data):
    #     return EmpPersonalDetailsModelSerializer.create(**validated_data)
        # return super().create(**validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, **validated_data)
