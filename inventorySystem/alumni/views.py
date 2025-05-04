from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response # TODO: check if this wil be needed
from rest_framework import status
from .serializer import AlumniSerializer
from .models import Alumni

# Create your views here.
@api_view(['GET'])
def alumniList(resquest) -> Response:  # TODO: check if the param is needed
    alumni = Alumni.objects.all()
    serializer = AlumniSerializer(alumni, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createAlumni(request) -> Response:
    serializer = AlumniSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateAlumni(request, id) -> Response:
    alumni = Alumni.objects.get(alumni_id=id)
    serializer = AlumniSerializer(instance=alumni, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteAlumni(resquest, id):
    try:
        alumni = Alumni.objects.get(alumni_id=id)
        alumni.delete()
        return HttpResponse({"message": "Alumni deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Alumni.DoesNotExist:
        return HttpResponse({"error": "Alumni not found"}, status=404)
    