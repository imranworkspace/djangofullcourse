from .models import SingerModel,SongModel
from rest_framework.viewsets import ModelViewSet
from .serializer import SongSerializer,SingerSerializer

class SingerView(ModelViewSet):
    queryset=SingerModel.objects.all()
    serializer_class=SingerSerializer

class SongView(ModelViewSet):
    queryset=SongModel.objects.all()
    serializer_class=SongSerializer
    