from django.shortcuts import render
from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(['GET'])
def all_stud(request):
    studall=StudentModel.objects.all()
    serializer=StudentSerializer(studall,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_stud(request,pk):
    try:
        stud_get=StudentModel.objects.get(id=pk)
    except:
        return Response({'message':f'{pk} user does not exist'},status=status.HTTP_200_OK)
    else:
        serializer = StudentSerializer(stud_get)
        return Response(serializer.data,status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def create_stud(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response({"response":"user created successfully"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors)



@api_view(['PUT'])
def stud_fullupdate(request, pk):
    try:
        student = StudentModel.objects.get(id=pk)
    except StudentModel.DoesNotExist:
        return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student, data=request.data)  # full update
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student fully updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def stud_update(request,pk):
    try:
        user=StudentModel.objects.get(id=pk)
    except StudentModel.DoesNotExist:
        return Response({"message":f"{pk} does not exist"},status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer=StudentSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)


@api_view(['DELETE'])
def del_stud(request,pk):
    try:
        StudentModel.objects.get(id=pk).delete()
    except StudentModel.DoesNotExist:
        return Response({"message":f"{pk} user does not exists"},status=status.HTTP_200_OK)
    else:
        return Response({"message":f"user deleted successfully which user is id {pk}"},status=status.HTTP_200_OK)
    