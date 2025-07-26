from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.CBV.as_view(),name='students'),
    path('students/<int:pk>/', views.CBV.as_view(),name='students'),
]
