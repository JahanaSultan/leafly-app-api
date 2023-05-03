from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teaware import views

router=DefaultRouter()
router.register('teaware', views.TeawareViewSet)
app_name='teaware'


urlpatterns = [
    path('', include(router.urls)),
]
