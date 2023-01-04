from .viewsets import RestLogModelViewSet
from .models import Plato
from .serializers import PlatoSerializer


class PlatoViewSet(RestLogModelViewSet):
    model = Plato
    serializer_class = PlatoSerializer
    queryset = Plato.objects.all()
