from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions

class StudentApiView(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    # locally defined
    '''authentication_classes=[BasicAuthentication] # asking for username and password to access apis
    permission_classes=[IsAdminUser]# only access which user has isstaff=True '''
    authentication_classes=[BasicAuthentication] 
    permission_classes=[IsAuthenticatedOrReadOnly] # only authorised person access anon user can see api only
    