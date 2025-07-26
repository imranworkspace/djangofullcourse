from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.viewsets import ModelViewSet
# custom permission
from .custom_permission import MyPermissionEx
from rest_framework.authentication import SessionAuthentication

class StudentApiView(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    # locally defined
    authentication_classes=[SessionAuthentication] # my custom authentication class 
    permission_classes=[MyPermissionEx] # my custom permission class