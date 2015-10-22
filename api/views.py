from OTW.models import Orden
from rest_framework.viewsets import ModelViewSet

from .serializers import OrdenSerializer


class OrdenView(ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
