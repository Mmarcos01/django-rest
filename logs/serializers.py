from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'title', 'body', 'created_at')
        model = Log
