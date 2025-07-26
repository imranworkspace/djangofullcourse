from django.contrib import admin
from django.urls import path
from api.views import StudentListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewall/',StudentListView.as_view()),
]
