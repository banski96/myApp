
from rest_framework import viewsets
from .serializer import EventSerializer
from .models import Events

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    lookup_field = "event_id"

