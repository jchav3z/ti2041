from rest_framework import generics
from django.shortcuts import render
from .models import Provider, Service
from .serializers import ProviderSerializer, ServiceSerializer

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.filter(thru_date__isnull=True)
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProviderDetail(generics.RetrieveAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

def service_list(request):
    services = Service.objects.filter(thru_date__isnull=True)
    return render(request, 'service_list.html', {'services': services})

