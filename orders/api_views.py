from django.shortcuts import render
from rest_framework import api_view
from rest_framework.response import Response
from rest_framework import decorators
from rest_framework import status
from .serializers import NotesSerializer
from .models import Notes
from django.contrib.admin import get_object_http404
# Create your views here.
@api_view(['GET'])
def post_list(request):
    #here is the python oject model
    post=Notes.objects.all()
    #here we serialize it to json for api response
    serializer=NotesSerializer(post,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail_list(request,post_id):
    post=Notes.objects.get(id=post_id)
    #will i pass the model here may posts=Notes.object.first()
    serializer=NotesSerializer(post)
    return Response(serializer.data)
@api_view(['POST'])
def create_post(request):
    #get the python object the models and serialize it json
    serializer=NotesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def update_post(request,post_id):
    post=Notes.objects.get(id=post_id)
    serializer=NotesSerializer(post,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_post(request,post_id):
    post=Notes.objects.get(id=post_id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
