from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Blogserial as Blog

# Create your views here.


class BlogView(APIView):

    def get(self, request):
        return 0

    def post(self, request):
        data = request.data
        serializer = Blog(data,many =True)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully added",status=201)
        return Response("failed",400)

    def put(self, request):
        return 0

    def delete(self, request):
        return 0
