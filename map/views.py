from django.shortcuts import render
from rest_framework import viewsets

from map.models import Well
from map.serializers import WellSerializer


class wellsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wells to be viewed or edited.
    """

    queryset = Well.objects.all()
    serializer_class = WellSerializer


