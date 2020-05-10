from rest_framework_mongoengine import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from .models import Secret


class SecretCreateSerialazer(DocumentSerializer):
    class Meta:
        model = Secret
        fields = ['text', 'pass_phrase']


class SecretGetSerialazer(DocumentSerializer):
    class Meta:
        model = Secret

