from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

class StudentApiView(viewsets.ViewSet):
    def list(self,request):
        try:
            studall=StudentModel.objects.all()
            serializer=StudentSerializer(studall,many=True)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data,status=status.HTTP_200_OK)
            
    def retrieve(self,request,pk=None):
            try:
                stud_get=StudentModel.objects.get(id=pk)
                serializer=StudentSerializer(stud_get)
            except:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = StudentSerializer(stud_get)
                return Response(serializer.data,status=status.HTTP_200_OK)


    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response({"response":"user created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def update(self,request,pk):
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)  # full update
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student fully updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        try:
            student = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return Response({"message": f"Student with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)  # full update
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student partially updated", "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(self,request,pk):
        try:
            StudentModel.objects.get(id=pk).delete()
        except StudentModel.DoesNotExist:
            return Response({"message":f"{pk} user does not exists"},status=status.HTTP_200_OK)
        else:
            return Response({"message":f"user deleted successfully which user is id {pk}"},status=status.HTTP_200_OK)
        