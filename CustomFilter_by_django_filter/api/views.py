from .models import StudentModel
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class StudentListView(ListAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    # filterset_fields=['city']
    filterset_fields=['city','passby']
    