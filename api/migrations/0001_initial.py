# Generated by Django 2.2.12 on 2020-05-10 12:09

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('secret_key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pass_phrase', models.CharField(max_length=90, verbose_name='Code Phrase')),
                ('text', models.TextField(verbose_name='Secter Text')),
                ('life_time', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]