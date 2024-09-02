from django.contrib import admin

# Register your models here.
from tutorial.models import Tache
from .models import Institution
class AdminPersonne(admin.ModelAdmin):
    list_display=('nom','price','description')
    #ce script permet d'enregistrer la table personne du coté administrateur de l'application
admin.site.register(Institution)
admin.site.register(Tache)
