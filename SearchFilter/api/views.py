from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.filters import SearchFilter

# Create your views here.

class StudentListCreateApiView(ListAPIView,CreateAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    search_fields=['city']
    # search_fields=['name','city']
    search_fields=['^name'] # search by initial
    
    # we can use 'q' instead of default 'search'
    '''REST_FRAMEWORK={
        'SEARCH_PARAM':'q'
    }'''


