from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentApiView(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    # locally defined
    authentication_classes=[TokenAuthentication] 
    permission_classes=[IsAuthenticated]
