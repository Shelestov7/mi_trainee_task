import uuid


from django.db import models
from django.db.models.functions import datetime
from django_cryptography.fields import encrypt


class Secret(models.Model):
    secret_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pass_phrase = models.CharField('Pass', max_length=200)
    text = models.TextField('text', max_length=200)
    life_time = models.DateTimeField(auto_now=True)



# default=uuid.uuid4, editable=False, binary=False