from api import views
from django.contrib import admin
from django.urls import path
# swagger implementation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Student API",# custom project name 
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.fbv_student,name='students'),
    path('students/<int:pk>/', views.fbv_student,name='students'),
    # swagger 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
