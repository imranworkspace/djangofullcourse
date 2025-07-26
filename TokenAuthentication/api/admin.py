from django.contrib import admin
from .models import StudentModel

@admin.register(StudentModel)
class StudentRegister(admin.ModelAdmin):
    list_display=['id','roll','name','email']
# Register your models here.
