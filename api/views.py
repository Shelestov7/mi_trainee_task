from .serializers import SecretCreateSerialazer, SecretGetSerialazer
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Secret


class SecretCreateView(ListCreateAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretCreateSerialazer


class SecretRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretGetSerialazer


import hashlib

# a = hashlib.sha256(secrets.encode('utf-8')).hexdigest()
