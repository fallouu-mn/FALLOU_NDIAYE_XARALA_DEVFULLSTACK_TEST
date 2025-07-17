from rest_framework import serializers
from .models import Bootcamp, Lead

class BootcampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    bootcamp_title = serializers.CharField(source='bootcamp.title', read_only=True)
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Lead
        fields = ['id', 'name', 'email', 'phone', 'message', 'status', 'created_at', 'bootcamp', 'bootcamp_title', 'updated_by']
