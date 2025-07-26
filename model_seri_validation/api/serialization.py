from rest_framework import serializers
from .models import StudentModel
from rest_framework.validators import UniqueValidator

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=['name','email','roll']

    # 2. Field Level Validation
    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError('seat full')
        return value

    # 3. Object Level Validation
    def validate(self,data):
        nm=data.get('name')
        em=data.get('email')
        if nm.lower()=='imran' and em.lower()!='imran@gmail.com':
            raise serializers.ValidationError('email should be imran@gmail.com')
        return data 
    

    

# validators should be defined begin on serializer class
# function should passed into respective field name where we want to use for validation using validators=[] inside list
# we can pass multiple functions inside validators=[] 
# Validators or Custom validator function
'''# ex.1
def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('name should be starts with r')
# ex.2 
def must_be_gmail(value):
    if "@gmail.com" not in value:
        raise serializers.ValidationError("Email must be a Gmail address")
'''


