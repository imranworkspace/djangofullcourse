from rest_framework import serializers
from .models import SingerModel,SongModel



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=SongModel
        fields=['id','title','duration']

class SingerSerializer(serializers.ModelSerializer):
    sungby=SongSerializer(many=True,read_only=True) # add entire child serializer to main 
    class Meta:
        model=SingerModel
        fields=['id','singer_name','gender','sungby']
    
    def get_gender_label(self, obj):
        return obj.get_gender_display()