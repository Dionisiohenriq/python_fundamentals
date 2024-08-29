# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.pokemon_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Trainers(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    trainer_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date_created')

    def __str__(self) -> str:
        return self.trainer_name

    def was_published_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)
