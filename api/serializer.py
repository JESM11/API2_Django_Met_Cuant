from rest_framework import serializers
from .models import Sim

class SimSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sim
        fields='__all__'