from django import forms
from .models import Pret

class TaskForm(forms.ModelForm):
  class Meta:
    model = Pret
    fields =['noms','addresse','phone_number','emprun','date_sortie','date_entree']