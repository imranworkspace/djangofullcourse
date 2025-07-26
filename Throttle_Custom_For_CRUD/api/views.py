from .models import StudentModel
from .serialization import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

class StudentViewAll(ListAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewall'

class StudentCreateView(CreateAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='create'

class StudentUpdateView(UpdateAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='update'

class StudentRetriveview(RetrieveAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='retrive'

class StudentDestroyView(DestroyAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='delete'


