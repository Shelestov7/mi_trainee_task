from rest_framework_mongoengine import serializers
from rest_framework import serializers

from .models import Secret


class SecretCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("pass_phrase", "text", 'life_time', 'secret_key')
        model = Secret


class SecretGetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("text",)
        model = Secret
