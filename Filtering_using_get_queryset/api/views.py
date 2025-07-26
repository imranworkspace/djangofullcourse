from .models import StudentModel
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication

class StudentListView(ListAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]

    def get_queryset(self):
        user=self.request.user
        return StudentModel.objects.filter(passby=user)