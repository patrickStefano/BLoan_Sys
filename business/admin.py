from django.contrib import admin
from .models import Pret

class TaskPret(admin.ModelAdmin):
    list_display = ('noms', 'adresse', 'phone_number','emprun','interet','total','date_sortie','date_entree','user_id','action')  # Add the fields you want to display

admin.site.register(Pret, TaskPret)

# Register your models here.
