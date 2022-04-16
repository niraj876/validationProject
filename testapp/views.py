import io

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StudentModel


# Create your views here.
# @csrf_exempt
# def create_student(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=python_data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):

    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        if id is not None:
            student = StudentModel.objects.get(id=id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data)
        student = StudentModel.objects.all()
        serializer = StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Student record created'}
            return JsonResponse(response)
        return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = StudentModel.objects.get(id=id)
        serializer = StudentSerializer(student, data = python_data)

        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'student record updated'}
            return JsonResponse(response)
        return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = StudentModel.objects.get(id = id)
        student.delete()
        response = {'msg': "Student record deleted"}
        return JsonResponse(response)


#
# @csrf_exempt
# def student(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#
#         if id is not None:
#             student = StudentModel.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             return JsonResponse(serializer.data)
#
#         student = StudentModel.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=python_data)
#
#         if serializer.is_valid():
#             serializer.save()
#             response = {'msg': 'Student record created'}
#             return JsonResponse(response)
#
#         return JsonResponse(serializer.errors)
#
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         student = StudentModel.objects.get(id=id)
#         serializer = StudentModel(student, data=python_data)
#
#         if serializer.is_valid():
#             serializer.save()
#             response = {'msg': 'Student record updated'}
#             return JsonResponse(response)
#         return JsonResponse(serializer.errors)
#
#     if request.method == 'delete':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         student = StudentModel.objects.get(id=id)
#         response = {'msg': 'Student record deleted'}
#         return JsonResponse(response)
#
