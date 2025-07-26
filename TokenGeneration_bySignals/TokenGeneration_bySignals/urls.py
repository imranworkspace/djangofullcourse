from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

# for generating token api
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('studentapi',views.StudentApiView,basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',obtain_auth_token),

]
