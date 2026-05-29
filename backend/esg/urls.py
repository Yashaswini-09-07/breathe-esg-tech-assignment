from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ActivityRecordViewSet

router = DefaultRouter()
router.register(r'records', ActivityRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
