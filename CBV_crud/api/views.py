from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# for put,post,patch
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# swagger implemention
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema


@method_decorator(csrf_exempt, name='dispatch')
class CBV(APIView):
    
    @swagger_auto_schema(
        operation_description="Get student by ID or all students",
        responses={200: StudentSerializer(many=True)}
    )
    def get(self, request, pk=None, format=None):
        if pk:
            try:
                student = StudentModel.objects.get(id=pk)
                serializer = StudentSerializer(student)
            except StudentModel.DoesNotExist:
                return Response({"message": f"Student with ID {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = StudentModel.objects.all()
            serializer = StudentSerializer(students, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=StudentSerializer,
        responses={201: "Created"}
    )
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=StudentSerializer,
        responses={202: "Updated"}
    )
    def put(self, request, pk, format=None):
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student fully updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=StudentSerializer,
        responses={202: "Partially Updated"}
    )
    def patch(self, request, pk, format=None):
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student partially updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={200: "Deleted"}
    )
    def delete(self, request, pk, format=None):
        try:
            student = StudentModel.objects.get(id=pk)
            student.delete()
            return Response({"message": f"User with ID {pk} deleted successfully"}, status=status.HTTP_200_OK)
        except StudentModel.DoesNotExist:
            return Response({"message": f"User with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)