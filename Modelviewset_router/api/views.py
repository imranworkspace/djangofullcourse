from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.viewsets import ModelViewSet


class StudentApiView(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer