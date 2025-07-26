from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.LCAPI.as_view(),name='students'),
    path('students/<int:pk>/', views.RUDAPI.as_view(),name='students'),
]
