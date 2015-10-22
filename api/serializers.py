from OTW.models import Orden
from rest_framework.serializers import ModelSerializer


class OrdenSerializer(ModelSerializer):

    class Meta:
        model = Orden
        fields = ('pk', 'cliente', 'estado',
                  'fechainicio', 'fechafin',
                  'observaciones', 'resolucion',
                  'responsable', 'solicitud')
