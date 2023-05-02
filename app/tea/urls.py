from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tea import views

router=DefaultRouter()
router.register('tea', views.TeaViewSet)
app_name='tea'


urlpatterns = [
    path('', include(router.urls)),
]
