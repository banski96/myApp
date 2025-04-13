from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response # TODO: check if this wil be needed
from rest_framework import status
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

@api_view(['GET'])
def viewByID(resquest, id):
    try:
        event = Events.objects.get(event_id=id)
    except Events.DoesNotExist:
        return HttpResponse({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def updateEvent(resquest, id):
    event = Events.objects.get(event_id=id)
    serializer = EventSerializer(instance=event, data=resquest.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteEvent(resquest, id):
    try:
        event = Events.objects.get(event_id=id)
        event.delete()
        return HttpResponse({"message": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Events.DoesNotExist:
        return HttpResponse({"error": "Event not found"}, status=404)