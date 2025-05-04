from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response # TODO: check if this wil be needed
from rest_framework import status
from .serializer import SpeakersSerializer
from .models import Speakers

# Create your views here.
@api_view(['GET'])
def speakerList(resquest) -> Response:  # TODO: check if the param is needed
    speaker = Speakers.objects.all()
    serializer = SpeakersSerializer(speaker, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createSpeakers(request) -> Response:
    serializer = SpeakersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateSpeakers(request, id) -> Response:
    speaker = Speakers.objects.get(speaker_id=id)
    serializer = SpeakersSerializer(instance=speaker, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSpeakers(resquest, id):
    try:
        speaker = Speakers.objects.get(speaker_id=id)
        speaker.delete()
        return HttpResponse({"message": "Speaker deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Speakers.DoesNotExist:
        return HttpResponse({"error": "Speaker not found"}, status=404)
    