from rest_framework import serializers
from .models import Events
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
    
    def validate(self, data):
        if data['start_date'] < timezone.now().date():
            raise serializers.ValidationError({"start_date": "Start date cannot be in the past."})
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({"start_date":"Start date should not be greater than end date"})
        return data