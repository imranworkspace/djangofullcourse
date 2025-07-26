from rest_framework import serializers
from .models import SingerModel,SongModel



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=SongModel
        fields=['id','title','duration']

class SingerSerializer(serializers.ModelSerializer):
    #song=serializers.StringRelatedField(many=True,read_only=True)
    #song=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    # song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    class Meta:
        model=SingerModel
        fields=['id','singer_name','gender','song']
    
    def get_gender_label(self, obj):
        return obj.get_gender_display()