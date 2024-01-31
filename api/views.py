from rest_framework import viewsets
from .models import Sim
from .serializer import SimSerializer

# Create your views here.

class SimViewSet(viewsets.ModelViewSet):
    queryset = Sim.objects.all()
    serializer_class = SimSerializer

