from OTW.models import AccionOrden, MaterialOrden, Orden
from rest_framework.viewsets import ModelViewSet

from .serializers import AccionSerializer, MaterialSerializer, OrdenSerializer


class OrdenView(ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class MaterialView(ModelViewSet):
    queryset = MaterialOrden.objects.all()
    serializer_class = MaterialSerializer


class AccionView(ModelViewSet):
    queryset = AccionOrden.objects.all()
    serializer_class = AccionSerializer
