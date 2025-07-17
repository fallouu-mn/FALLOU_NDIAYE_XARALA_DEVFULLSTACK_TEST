from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Bootcamp, Lead
from .serializers import BootcampSerializer, LeadSerializer

class BootcampList(generics.ListAPIView):
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer
    permission_classes = [permissions.AllowAny]  # Public

class BootcampDetail(generics.RetrieveAPIView):
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer
    permission_classes = [permissions.AllowAny]  # Public

class LeadCreate(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.AllowAny]  # Public
class LeadList(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]  # Admin seulement



    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        # Ajoute le titre du bootcamp pour chaque lead
        data = serializer.data
        for lead in data:
            lead['bootcamp_title'] = Bootcamp.objects.get(id=lead['bootcamp']).title
        
        return Response(data)

class LeadUpdate(generics.UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]  # Admin seulement
    http_method_names = ['patch']  # Restreint aux PATCH

    def perform_update(self, serializer):
        # Journalise qui a modifié le lead
        serializer.save(updated_by=self.request.user)