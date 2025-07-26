from django.contrib import admin
from django.urls import path
from api.views import StudentListCreateApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewall/',StudentListCreateApiView.as_view(),name='viewall')
]
