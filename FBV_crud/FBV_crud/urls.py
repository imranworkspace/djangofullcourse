from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.fbv_student,name='students'),
    path('students/<int:pk>/', views.fbv_student,name='students'),
]
