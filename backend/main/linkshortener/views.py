from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import MyLink
from .serializer import LinkSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def link_shortener(request):
  serializer = LinkSerializer(data=request.data)
  if serializer.is_valid():
    if request.user.is_anonymous:
      serializer.save()
    else:
      serializer.save(user=request.user)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_links(request):
  links = MyLink.objects.filter(user=request.user)
  serializer = LinkSerializer(links, many=True) 
  return Response(serializer.data)


@api_view(['GET'])
def get_link(request, hash):
  link = get_object_or_404(MyLink, hash=hash)
  serializer = LinkSerializer(link, many=False)
  return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_link(request, hash):
  link = get_object_or_404(MyLink, hash=hash)
  link.delete()
  return Response('Link deleted.')







