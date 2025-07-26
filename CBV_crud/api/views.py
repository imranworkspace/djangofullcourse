from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# for put,post,patch
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt,name='dispatch')
class CBV(APIView):
    def get(self,request,pk=None,format=None):
        try:
            stud_get=StudentModel.objects.get(id=pk)
        except:
            studall=StudentModel.objects.all()
            serializer=StudentSerializer(studall,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            serializer = StudentSerializer(stud_get)
            return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response({"response":"user created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self,request,pk,format=None):
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)  # parital update
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student fully updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)  # full update
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student partially updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk,format=None):
        try:
            StudentModel.objects.get(id=pk).delete()
        except StudentModel.DoesNotExist:
            return Response({"message":f"{pk} user does not exists"},status=status.HTTP_200_OK)
        else:
            return Response({"message":f"user deleted successfully which user is id {pk}"},status=status.HTTP_200_OK)
        