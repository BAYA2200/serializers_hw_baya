from rest_framework import serializers

from . import models
from .models import Employee, Status


class StatusSerializers(serializers.Serializer):
    class Meta:
        model = Status
        fields = '__all__'


class EmployeeSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    birth_year = serializers.CharField(max_length=100)
    position_id = serializers.IntegerField()
    salary = serializers.CharField(max_length=100)
