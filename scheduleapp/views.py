from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ProtectedScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]
