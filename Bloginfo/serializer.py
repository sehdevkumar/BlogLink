from rest_framework import serializers
from .models import Blog

class Blogserial(serializers.Serializer):
    title = serializers.CharField()
    blogtext = serializers.CharField()
    date = serializers.DateField()
    
    def Create(self, validated_data):
        return Blog.objects.create(**validated_data)
    
