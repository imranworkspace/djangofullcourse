from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
# custom class 
from .myPagination import MyPageNumberPagination 

class StudentListCreateApiView(ListAPIView,CreateAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyPageNumberPagination
    
    

