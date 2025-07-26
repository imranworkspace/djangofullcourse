from .models import StudentModel
from .serialization import StudentSerializer
# for put,post,patch
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# for genericapiview 
from rest_framework.generics import GenericAPIView
# for mixin
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin

#@method_decorator(csrf_exempt,name='dispatch')
class StudentGet(GenericAPIView,ListModelMixin):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwagrs):
        return self.list(request,*args,**kwagrs)

class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwagrs):
        return self.retrieve(request,*args,**kwagrs)


class StudentPost(GenericAPIView,CreateModelMixin):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    def post(self,request,*args,**kwagrs):
        return self.create(request,*args,**kwagrs)

class StudentPut(GenericAPIView,UpdateModelMixin):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,*args,**kwagrs):
        return self.update(request,*args,**kwagrs)

class StudentPatch(GenericAPIView,UpdateModelMixin):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    def patch(self,request,*args,**kwagrs):
        return self.partial_update(request,*args,**kwagrs)

class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request,*args,**kwagrs):
        return self.destroy(request,*args,**kwagrs)

