from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.viewsets import ModelViewSet
# custom permission
from rest_framework.permissions import IsAuthenticated
# custom authentication
from api.custom_authentication import CustomBaseAuthentication

class StudentApiView(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    # locally defined
    authentication_classes=[CustomBaseAuthentication] # my custom authentication class 
    permission_classes=[IsAuthenticated] 