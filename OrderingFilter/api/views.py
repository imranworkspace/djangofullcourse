from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.filters import OrderingFilter

# Create your views here.

class StudentListCreateApiView(ListAPIView,CreateAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[OrderingFilter]
    # ordering_fields=['name'] 
    ordering_fields=['name','city'] 
    
    
    

