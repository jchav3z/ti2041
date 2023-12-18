from rest_framework import serializers
from .models import Provider, Contact, Address, Service

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    addresses = AddressSerializer(many=True)
    services = ServiceSerializer(many=True)

    class Meta:
        model = Provider
        fields = '__all__'
