from rest_framework import viewsets
from .models import ActivityRecord
from .serializers import ActivityRecordSerializer


class ActivityRecordViewSet(viewsets.ModelViewSet):
    queryset = ActivityRecord.objects.all()
    serializer_class = ActivityRecordSerializer