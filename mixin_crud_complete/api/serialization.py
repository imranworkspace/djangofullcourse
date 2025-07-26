from rest_framework import serializers
from .models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__'

    # form field validation
    def validate_roll(self,value):
        if value>10:
            raise serializers.ValidationError('seat full try next time !!!')
        return value 
    
    # form field validation
    def validate_name(self,value):
        if value[0]!='i':
            raise serializers.ValidationError('name should be start with "i" !!!')
        return value    

    # object field validation
    def validate(self,data):
        nm=data.get('name') 
        em=data.get('email') 
        if nm=='imran' and em!='imran@gmail.com':
            raise serializers.ValidationError('email should be "imran@gmail.com"')
        return data