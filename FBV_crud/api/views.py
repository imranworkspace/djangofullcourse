from django.shortcuts import render
from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# USE authentication and permission classes in FBV
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET','POST','PUT','PATCH'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def fbv_student(request,pk=None):
    
    if request.method=='GET':
        try:
            stud_get=StudentModel.objects.get(id=pk)
        except:
            studall=StudentModel.objects.all()
            serializer=StudentSerializer(studall,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            serializer = StudentSerializer(stud_get)
            return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response({"response":"user created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method=='PUT':
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)  # full update
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student fully updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method=='PATCH':
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)  # full update
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student partially updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method=='DELETE':
        try:
            StudentModel.objects.get(id=pk).delete()
        except StudentModel.DoesNotExist:
            return Response({"message":f"{pk} user does not exists"},status=status.HTTP_200_OK)
        else:
            return Response({"message":f"user deleted successfully which user is id {pk}"},status=status.HTTP_200_OK)
        