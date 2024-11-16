from django.db import models
from django.contrib.auth.models import User

class Pret(models.Model):
  noms = models.CharField(max_length=50)
  adresse = models.TextField()
  
  phone_number = models.CharField(max_length=15, unique=True) 
  # Automatically set the field to now when the object is first created
  emprun = models.CharField(max_length=10, unique=True)
  interet = models.CharField(max_length=10, unique=True)
  total = models.CharField(max_length=10, unique=True)
  date_sortie = models.DateField()
  date_entree = models.DateField()
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  action = models.BooleanField(default=False)


  def __str__(self):
    return self.noms
  

# Create your models here.
