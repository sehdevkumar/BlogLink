from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView

# Create your views here.


class BlogView(APIView):
    def get(self, request):
        return 0

    def post(self, request):
        return 0

    def put(self, request):
        return 0

    def delete(self, request):
        return 0
