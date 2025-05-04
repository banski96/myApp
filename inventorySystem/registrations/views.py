from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response # TODO: check if this wil be needed
from rest_framework import status
from .serializer import RegistrationsSerializer
from .models import Registrations

# Create your views here.
@api_view(['GET'])
def registrationList(resquest) -> Response:  # TODO: check if the param is needed
    registration = Registrations.objects.all()
    serializer = RegistrationsSerializer(registration, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createRegistration(request) -> Response:
    serializer = RegistrationsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateRegistration(request, id) -> Response:
    registration = Registrations.objects.get(registration_id=id)
    serializer = RegistrationsSerializer(instance=registration, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteRegistration(resquest, id):
    try:
        registration = Registrations.objects.get(registration_id=id)
        registration.delete()
        return HttpResponse({"message": "Registration deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Registrations.DoesNotExist:
        return HttpResponse({"error": "Registration not found"}, status=404)
    