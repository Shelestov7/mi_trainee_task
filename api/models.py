import uuid
from datetime import datetime
from mongoengine import *
from mongoengine import connect
connect('api')


class Secret(Document):
    secret_key = UUIDField(primary_key=True, default=uuid.uuid4, editable=False, binary=False)
    pass_phrase = StringField('Code Phrase', max_length=90, allow_blank=True)
    text = StringField('Secret Text', max_length=1000, allow_blank=True)
    life_time = DateTimeField(default=datetime.utcnow)



