from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.viewsets import ModelViewSet
# custom permission
from rest_framework.permissions import IsAuthenticated
# custom JWT token
from rest_framework_simplejwt.authentication import JWTAuthentication
class StudentApiView(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    # locally defined
    authentication_classes=[JWTAuthentication] # my custom authentication class 
    permission_classes=[IsAuthenticated] 