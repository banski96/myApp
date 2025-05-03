from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response # TODO: check if this wil be needed
from rest_framework import status
from .serializer import ProgramSerializer
from .models import Programs

# Create your views here.
@api_view(['GET'])
def programList(resquest) -> Response:  # TODO: check if the param is needed
    proram = Programs.objects.all()
    serializer = ProgramSerializer(proram, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createProgram(request) -> Response:
    serializer = ProgramSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateProgram(request, id) -> Response:
    program = Programs.objects.get(program_id=id)
    serializer = ProgramSerializer(instance=program, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProgram(resquest, id):
    try:
        program = Programs.objects.get(program_id=id)
        program.delete()
        return HttpResponse({"message": "Program deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Programs.DoesNotExist:
        return HttpResponse({"error": "Program not found"}, status=404)