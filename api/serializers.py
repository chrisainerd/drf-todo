# api/serializers.py
from rest_framework import serializers
from todo import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'complete',
        )
        model = models.Todo