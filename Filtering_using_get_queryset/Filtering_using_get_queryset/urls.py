from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewall/',views.StudentListView.as_view(),name='viewall'),
    path('auth/',include("rest_framework.urls"))
]
