from OTW.models import AccionOrden, MaterialOrden, Orden
from rest_framework.serializers import ModelSerializer


class MaterialSerializer(ModelSerializer):

    class Meta:
        model = MaterialOrden


class AccionSerializer(ModelSerializer):

    class Meta:
        model = AccionOrden


class OrdenSerializer(ModelSerializer):
    material = MaterialSerializer(many=True, read_only=True)
    acciones = AccionSerializer(many=True, read_only=True)

    class Meta:
        model = Orden
        fields = ('pk', 'cliente', 'estado',
                  'fechainicio', 'fechafin',
                  'observaciones', 'resolucion',
                  'responsable', 'solicitud',
                  'material', 'acciones')
