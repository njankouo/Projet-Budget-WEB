from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from tutorial.forms import TacheForm
from tutorial.models import Tache
# Create your views here.
from django.http import HttpResponse
from .models import *

import io
from django.http import HttpResponse
from django.http import FileResponse
import os
def Home(request):
    institution=Institution.objects.order_by('-id')
    count=Institution.objects.all().count()
    context={
        'institution':institution,
        'count':count
    }
    template="../website/authentification/login.html"
    return render(request,template,context)

def Task(request):
    template="../website/task.html"
    return render(request,template)

def Operation(request):
    template="../website/operation.html"
    return render(request,template)


def list_taches(request):
    taches = Tache.objects.all()
    return render(request, 'list_taches.html', {'taches': taches})



def tache(request):
    template = "../website/tache.html"
    tache = Tache.objects.all()
    context= {'tache':tache}
    return render(request,template,context)

def delete_tache(request,id):
    tache = Activite.objects.get(idactivite=int(id))
    tache.delete()
    return redirect('/tache/')

def new_tache(request):
    

    template = "../website/forms/newtache.html"
    sous_programme = Sousprogramme.objects.all()
    activite = Activite.objects.all()
    context={'sous_programme':sous_programme,'activite':activite}
   
   
    
    
    
   
    return render(request,template,context)
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404  
from django.core.exceptions import ValidationError  # Import for validati


def sous_programme(request):
    template ='../website/sous_programme.html'
    sous_programme = Sousprogramme.objects.all()
    context={'sous_programme':sous_programme}
    return render(request,template,context)

def add_sous_programme(request):
    template = '../website/form_sous_programme.html'
    return render(request,template)

def save_Sous_programme(request):  
    if request.method == 'POST':  
        try:  
            nom = request.POST['nom']  
            libelle = request.POST['libelle']  
            indicateur = request.POST['indicateur']  
            print(f"Nom: {nom}, Libelle: {libelle}, Indicateur: {indicateur}")  

            save_sousprogramme = Sousprogramme.objects.create(nom=nom, libelleobjectif=libelle, libelleindicateur=indicateur)  
            save_sousprogramme.save()  
            messages.success(request, 'Sous-Programme Enregistre Avec Succes!')  
            return redirect('/sous_programme/')  
        except Exception as e:  
            print(f"Erreur: {e}")  
            messages.error(request, 'Une Erreur Est Survenue')  
            return redirect('/sous_programme/')  
    return redirect('/sous_programme/')

def activites(request):
    template ='../website/activite.html'
    activite=Activite.objects.all()
    context={'activite':activite}
    return render(request,template,context)

def add_activite(request):
    sous_Programme=Sousprogramme.objects.all()
    context={'sous_Programme':sous_Programme}
    template ='../website/forms/ActivityForm.html'
    return render(request,template,context)

def save_activity(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            indicateur = request.POST['indicateur']
            objectif = request.POST['objectif']
            sous_programme_id = request.POST['sous_programme']

            # Récupérer l'instance de Sousprogramme
            sous_programme_instance = Sousprogramme.objects.get(id=sous_programme_id)
            print(sous_programme_instance)

            # Créer l'activité avec l'instance de Sousprogramme
            save_activite = Activite.objects.create(
                nom=nom,
                idsousprogramme=sous_programme_instance,
                libelleindicateur=indicateur,
                libelleobjectif=objectif
            )
            save_activite.save()
            messages.success(request, 'Activite Enregistrée Avec Succès !')
            return redirect('/activites/')
        except Sousprogramme.DoesNotExist:
            messages.error(request, 'Le sous-programme spécifié n\'existe pas.')
            return redirect('/activites/')
        except Exception as e:
            messages.error(request, 'Une erreur est survenue...')
            print(f"Erreur: {e}")  
            return redirect('/activites/')
    return redirect('/activites/')

def users(request):
    template='../website/forms/compte.html'
    return render(request,template)

def save_taches(request):
    if request.method == 'POST':
        try:
        
            nom= request.POST['nom']
            objectif = request.POST['objectif']
            indicateur = request.POST['indicateur']
            activite = request.POST['activite']
            sousprogramme = request.POST['sousprogramme']
            instance_sous_programme = Sousprogramme.objects.get(id=int(sousprogramme))
            instance_activite = Activite.objects.get(id=int(activite))
            save_tache = Tache.objects.create(nom=nom,idsousprogramme=instance_sous_programme,idactivite=instance_activite,libelleobjectif=objectif,libelleindicateur=indicateur)
            save_tache.save()
            messages.success(request,'Tache Enregistre Avec Succes !')
            return redirect('/tache/')
        except Activite.DoesNotExist:
            messages.error(request,'Activite Inexistante')
        except Sousprogramme.DoesNotExist:
            messages.error(request,'Sous-Programme Inexistant')
        except Exception as e:
            messages.error(request,'Une Erreur Est Survenue')
            print(f"une erreur: {e}")
            return redirect('/tache/')
    return redirect('/tache/')

def operations(request):
    template = '../website/operations_list.html'
    return render(request,template)