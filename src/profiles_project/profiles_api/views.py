from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


from . import serializers
from . import models
from . import permissions
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

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello World"""
        a_viewset = [
        'Uses actions (list, create, retrieve, update, partial_update)',
        'Automatically maps to URLS using Routers',
        'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new Hello Message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, response, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method':'GET'})

    def update(self, response, pk=None):
        """Handle updating an object"""

        return Response({'http_method':'PUT'})

    def partial_update(self, response, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method':'PATCH'})

    def destroy(self, response, pk=None):
        """Handle removing an object"""

        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """Check email and password and return auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)
