from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import SongView,SingerView

router = DefaultRouter()
router.register('singer',SingerView,basename='singer')
router.register('song',SongView,basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
