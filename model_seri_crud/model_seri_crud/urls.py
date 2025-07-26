from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.all_stud,name='students'),
    path('student/<int:pk>/', views.get_stud, name='student'),
    path('partial_update/<int:pk>/', views.stud_update, name='partial_update'),
    
    path('fullupdate/<int:pk>/', views.stud_fullupdate, name='fullupdate'),
    path('delete/<int:pk>/', views.del_stud, name='delete'),
    path('create/', views.create_stud, name='create_stud'),
]
