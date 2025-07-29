from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from .models import StudentModel
from .serialization import StudentSerializer


@swagger_auto_schema(
    method='post',
    request_body=StudentSerializer,
    responses={201: "Created"}
)
@swagger_auto_schema(
    method='put',
    request_body=StudentSerializer,
    responses={202: "Updated"}
)
@swagger_auto_schema(
    method='patch',
    request_body=StudentSerializer,
    responses={202: "Partially Updated"}
)
@swagger_auto_schema(
    method='delete',
    request_body=None,
    responses={200: "Deleted"}
)
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def fbv_student(request, pk=None):
    if request.method == 'GET':
        try:
            student = StudentModel.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except StudentModel.DoesNotExist:
            students = StudentModel.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "user created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student fully updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student partially updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        try:
            StudentModel.objects.get(id=pk).delete()
            return Response({"message": f"User with ID {pk} deleted successfully"}, status=status.HTTP_200_OK)
        except StudentModel.DoesNotExist:
            return Response({"message": f"User with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
