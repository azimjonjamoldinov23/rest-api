from django.shortcuts import render
from myapp.models import Students
from rest_framework.generics import ListCreateAPIView ,ListAPIView , DestroyAPIView, RetrieveUpdateAPIView
from myapp.serializers import Studentsserializers , addStudentsserializers

# Create your views here.

class StudentsListAPIView(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentsserializers

class StudentsListCreateAPIView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = addStudentsserializers

class StudentsDestroyAPIView(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = Studentsserializers

class StudentsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = addStudentsserializers