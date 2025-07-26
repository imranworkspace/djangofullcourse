from rest_framework import serializers
from .models import StudentModel
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__' 

'''class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=25)
    email=serializers.EmailField() '''


    # below code requires only if serializers.Serializer
    # for post data, or for creating new record into db
'''def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance
'''


        
    

    