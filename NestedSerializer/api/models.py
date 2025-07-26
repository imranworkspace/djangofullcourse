from django.db import models

GENDER_CHOICES=[
    ('m','male'),
    ('f','female'),
    ('t','transgender'),
]

# Create your models here.
class SingerModel(models.Model):
    singer_name=models.CharField(max_length=25)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)

    def __str__(self) -> str:
        return self.singer_name

class SongModel(models.Model):
    title=models.CharField(max_length=15)
    duration=models.IntegerField()
    song=models.ForeignKey(SingerModel,on_delete=models.CASCADE,related_name='sungby') # 'related_name' is VIMP for SerializerRelatedFields

    def __str__(self) -> str:
        return self.title