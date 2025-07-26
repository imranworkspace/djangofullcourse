from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle
# custom throttle
from .throttle_custom import ImranUserThrottle


class StudentApiView(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,ImranUserThrottle]