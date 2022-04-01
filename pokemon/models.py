from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    type = models.CharField(max_length=100)
    # Model the many to one relationship
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    level = models.IntegerField(null=True)


