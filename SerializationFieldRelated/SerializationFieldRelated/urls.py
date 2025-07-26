from django.contrib import admin
from django.urls import path,include
from api.views import SingerView,SongView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('singer',SingerView,basename='singer')
router.register('song',SongView,basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
