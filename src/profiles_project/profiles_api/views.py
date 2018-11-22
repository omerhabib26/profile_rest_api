from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format = None):
        """Return a list of APIView feature"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Its is similar to a traditional Django view',
            'Gives you the most control over logic',
            'Is mapped manually on URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
