from rest_framework import viewsets
from .serializers import  VillainSerializer
from .models import Villain

class VillainViewSet(viewsets.ModelViewSet):
    queryset = Villain.objects.all().order_by('name')
    serializer_class = VillainSerializer

