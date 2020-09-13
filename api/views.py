import os
from cryptography.fernet import Fernet
from django.http import JsonResponse
from dotenv import load_dotenv
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    SecretCreateSerializer,
    SecretGetSerializer)
from rest_framework.generics import \
    (CreateAPIView,
     RetrieveAPIView, get_object_or_404)
from .models import Secret

load_dotenv()

key = bytes(os.getenv('KEY'), 'utf-8')
fernet = Fernet(key)


class SecretCreateView(CreateAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretCreateSerializer

    def perform_create(self, serializer):
        text = bytes(self.request.data['text'], 'utf-8')
        pass_phrase = bytes(self.request.data['pass_phrase'], 'utf-8')
        encrypt_text = fernet.encrypt(text)
        encrypt_phrase = fernet.encrypt(pass_phrase)
        serializer.save(text=encrypt_text, pass_phrase=encrypt_phrase)




class SecretRetrieveView(RetrieveAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretGetSerializer

    def get(self, request, *args, **kwargs):
        encrypt_text = Secret.pass_phrase
        return Response()
        if fernet.encrypt(bytes(request.data['pass_phrase'], 'utf-8')) == Secret.objects.all():
            return Response('jr')









    # def retrieve(self, request, pk):
    #     pass
    # # pass_phrase = bytes(request.GET.get('phrase'), 'utf-8')
    # # encrypt_pass_phrase = fernet.encrypt(pass_phrase)
    # encrypt_pass_phrase = request.GET.get('phrase')
    # instance = self.get_object()
    #
    # if bytes(instance.pass_phrase, ) == encrypt_pass_phrase:
    #     serializer = self.get_serializer(instance)
    #     print(type(serializer.data['text']))
    #     return Response(fernet.decrypt(serializer.data['text']).decode())
    # return Response({})
    # instance = self.get_object()
    # if pass_phrase ==instance.pass_phrase:
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    # else:
    #     ValueError
