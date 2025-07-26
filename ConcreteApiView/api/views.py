from .models import StudentModel
from .serialization import StudentSerializer
# for genericapiview 
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

class LCAPI(ListAPIView,CreateAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer

class RUD(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
