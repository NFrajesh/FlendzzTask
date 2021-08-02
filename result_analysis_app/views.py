from django.shortcuts import render
from .models import Students,StudentsMarks
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentsMarksSerializers,StudentsSerializers   

#<--------------------------/api/students/Details/----------------------------------->
@api_view(['GET'])
def Home(request):
    students = Students.objects.all()
    serializer =StudentsSerializers (students, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def Detail(request, pk):
    student = Students.objects.get(id=pk)
    serializer = StudentsSerializers(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddStudent(request):
    serializer = StudentsSerializers(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Update(request,pk):
    student = Students.objects.get(id=pk)
    serializer = StudentsSerializers(instance = student,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#<--------------------------/api/students/marks/----------------------------------->

@api_view(['GET'])
def GetMarks(request):
    student_marks=StudentsMarks.objects.all()
    serializer=StudentsMarksSerializers(student_marks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMark(request,pk):       
    student_mark=StudentsMarks.objects.get(id=pk)
    serializer=StudentsMarksSerializers(student_mark,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddMarks(request,pk):
    student_mark=StudentsMarks.objects.get(id=pk)
    serializer=StudentsMarksSerializers(instance=student_mark,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


 #<--------------------------/api/students/results/----------------------------------->

@api_view(['GET'])
def getResult(request):
    count = StudentsMarks.objects.count()
    Grade_A = StudentsMarks.objects.filter(grade='A').count()
    Grade_B = StudentsMarks.objects.filter(grade='B').count()
    Grade_C = StudentsMarks.objects.filter(grade='C').count()
    Grade_D = StudentsMarks.objects.filter(grade='D').count()
    Grade_E = StudentsMarks.objects.filter(grade='E').count()
    Grade_F = StudentsMarks.objects.filter(grade='F').count()
    Distinction = round(int(Grade_A)/int(count),2)
    FirstClassPercentage = round((int(Grade_B)+int(Grade_C))/int(count),2)
    PassPercentage = round((int(count)-int(Grade_F))/int(count),2)
    return Response(
        {
            "Total number of students":count,
            "number of students in Grade A ": Grade_A,
            "number of students in Grade B ": Grade_B,
            "number of students in Grade C ": Grade_C,
            "number of students in Grade D ": Grade_D,
            "number of students in Grade E ": Grade_E,
            "number of students in Grade F ": Grade_F,
            "Distinction (%)":Distinction,
            "First class (%)":FirstClassPercentage,
            "Pass (%)": PassPercentage
        })





# Create your views here.
