from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from .models import Employee, Status
from .serializers import EmployeeSerializers, StatusSerializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def status_list(request):
    if request.method == 'GET':
        statust = Employee.objects.all()
        serializers = EmployeeSerializers(statust, many=True)
        return JsonResponse(serializers.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class StatusListCreateAPIView(ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializers




