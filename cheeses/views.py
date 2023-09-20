from .models import Cheese
from rest_framework import viewsets, permissions
from .serializers import CheeseSerializer

# Create your views here.
class CheeseViewSet(viewsets.ModelViewSet):
    queryset = Cheese.objects.all()
    serializer_class = CheeseSerializer
    permission_classes = [permissions.AllowAny]