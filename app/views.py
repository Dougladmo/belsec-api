from rest_framework import viewsets

from app.models import Report
from app.serializers import ReportSerializer

# Create your views here.
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
