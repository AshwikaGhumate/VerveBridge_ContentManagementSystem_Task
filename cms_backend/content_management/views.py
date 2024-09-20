from rest_framework import viewsets
from .models import Page
from .serializers import PageSerializer
from rest_framework.permissions import IsAuthenticated

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]







