from typing import OrderedDict
from rest_framework import status
from django.db.models.query_utils import Q
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .permissions import IsOwner
from rest_framework import viewsets, mixins

from sensor_data.models import MeasurementType, Record, SensorData
from sensor_data.serializers import MeasurementTypeSerializer, RecordSerializer, SensorDataSerializer

from users.models import Patient

class HelloView(APIView):

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class SensorDataViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated & (IsOwner|IsAdminUser)]


    def get_queryset(self):
        if not self.request.user.is_staff:
            self.queryset = self.queryset.filter(Q(patient__user=self.request.user)|Q(patient__doctors__user=self.request.user))
        
        if self.request.query_params.get('patient_id'):
            self.queryset = self.queryset.filter(patient_id=self.request.query_params.get('patient_id'))
        
        return self.queryset

    def create(self, request, *args, **kwargs):
        data = OrderedDict()
        data.update(request.data)
        data["patient"] = get_object_or_404(Patient, user=self.request.user).id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MeasurementTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementTypeSerializer
    permission_classes = [AllowAny]

class RecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated & (IsOwner|IsAdminUser)]

    def get_queryset(self):
        if not self.request.user.is_staff:
            self.queryset = self.queryset.filter(Q(sensor_data__patient__user=self.request.user)|Q(sensor_data__patient__doctors__user=self.request.user))
        
        if self.request.query_params.get('patient_id'):
            self.queryset = self.queryset.filter(sensor_data__patient_id=self.request.query_params.get('patient_id'))
        if self.request.query_params.get('type'):
            self.queryset = self.queryset.filter(measurement_type__type=self.request.query_params.get('type'))

        
        return self.queryset
