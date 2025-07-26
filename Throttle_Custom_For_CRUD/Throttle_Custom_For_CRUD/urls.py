from django.contrib import admin
from django.urls import path
from api.views import StudentViewAll,StudentCreateView,StudentDestroyView,StudentUpdateView,StudentRetriveview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewall/', StudentViewAll.as_view()),
    path('create/', StudentCreateView.as_view()),
    path('retrive/<int:pk>/', StudentRetriveview.as_view()),
    path('update/<int:pk>/', StudentUpdateView.as_view()),
    path('delete/<int:pk>/', StudentDestroyView.as_view()),
]
