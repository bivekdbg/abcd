from rest_framework import serializers
from .models import DreamReal


class DreamRealSerializer(serializers.ModelSerializer):
    class Meta:
        model = DreamReal
        fields = "__all__"
