from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from rest_framework import status
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Return a list of APIView feature"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Its is similar to a traditional Django view',
            'Gives you the most control over logic',
            'Is mapped manually on URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello Message with our name."""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put (self, request, pk=None):
        """Handle updating an object."""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch Request, only database to update fields provided in the request."""

        return Response({'method':'Patch'})

    def delete(self, respone, pk=None):
        """Deletes an object."""

        return Response({'method':'delete'})



class HelloViewSet(viewsets.ViewSet):
    """Test API Viewsets."""

    def list(self, request):
        """Return a Hello World"""
        a_viewset = [
        'Uses actions (list, create, retrieve, update, partial_update)',
        'Automatically maps to URLS using Routers',
        'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewset' : a_viewset})
