from app.models import Report

from rest_framework import serializers

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'tipo', 'description', 'address', 'time', "image"]
