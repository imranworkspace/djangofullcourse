from django.contrib import admin
from .models import SingerModel,SongModel
# Register your models here.
@admin.register(SingerModel)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','singer_name','gender']

@admin.register(SongModel)
class SongModel(admin.ModelAdmin):
    list_display=['id','title','duration','song']
