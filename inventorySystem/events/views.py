from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response # TODO: check if this wil be needed
from .serializer import EventSerializer
from .models import Events

def appOverview(request):
    return JsonResponse("API HERE", safe=False)

@api_view(['GET'])
def eventList(resquest):  # TODO: check why does the pgadmin does not change only the postgres_data
    events = Events.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createEvent(resquest):
    serializer = EventSerializer(data=resquest.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)