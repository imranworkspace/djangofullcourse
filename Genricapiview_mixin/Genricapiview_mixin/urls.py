from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.StudentGet.as_view(),name='students'),
    #path('students/',views.StudentPost.as_view(),name='students'),
    #path('students/<int:pk>/',views.StudentRetrive.as_view(),name='students'),
    #path('students/<int:pk>/',views.StudentPut.as_view(),name='students'),
    path('students/<int:pk>/',views.StudentPatch.as_view(),name='students'),
    #path('students/<int:pk>/',views.StudentDelete.as_view(),name='students'),
]
