from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = DefaultRouter()
router.register('studentapi',views.StudentApiView,basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get_token/',TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token_refresh/',TokenRefreshView.as_view(),
         name='token_refresh_pair'),
    path('token_verify/',TokenVerifyView.as_view(),
         name='token_verify_pair'),
]
