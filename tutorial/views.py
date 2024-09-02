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
    institution=Institution.objects.order_by('-idinstitution')
    count=Institution.objects.all().count()
    context={
        'institution':institution,
        'count':count
    }
    template="../website/index.html"
    return render(request,template,context)

def Task(request):
    template="../website/task.html"
    return render(request,template)

def Operation(request):
    template="../website/operation.html"
    return render(request,template)

def create_operation(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_operation')  # Replace with your success URL
    else:
        form = TacheForm()
    
    return render(request, 'create_tache.html', {'form': form})

def list_taches(request):
    taches = Tache.objects.all()
    return render(request, 'list_taches.html', {'taches': taches})



def tache(request):
    template = "../website/tache.html"
    tache = Activite.objects.all()
    context= {'tache':tache}
    return render(request,template,context)

def delete_tache(request,id):
    tache = Activite.objects.get(idactivite=int(id))
    tache.delete()
    return redirect('/tache/')

def new_tache(request):
    

    template = "../website/new_tache.html"
    departement =Departement.objects.all()
    structure= Structure.objects.all()
    article= Article.objects.all()
    typestructure = Typestructure.objects.all()
    action = Action.objects.all()
    rangs = Rang.objects.all()
    context= {'structure':structure,'departement':departement,'article':article,'typestructure':typestructure,'action':action,'rangs':rangs}
    return render(request,template,context)
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404  
from django.core.exceptions import ValidationError  # Import for validati
def save_tache(request):
    if request.method == "POST":
        # Data retrieval
        code = request.POST['code']
        nom = request.POST['nom']
        structure_id = request.POST['structure']
        rang_id = request.POST['rang']
        action_id = request.POST.get('action')  # Get the action ID from the form
        justification = request.POST.get('justification', 'off') == 'on'

        # Retrieve corresponding objects
        structure = get_object_or_404(Structure, idstructure=structure_id)
        rang = get_object_or_404(Rang, idrang=rang_id)

        # Retrieve the Action object (handle potential errors)
        action = None
        if action_id:
            try:
                action = get_object_or_404(Action, idaction=action_id)
            except (DoesNotExist, ValidationError) as e:
                # Handle exceptions (e.g., action not found, validation error)
                messages.error(request, f"Erreur : Action introuvable (ID: {action_id})")
                return render(request, 'your_template.html', {'form': your_form})

        # Create a new Activite instance with the retrieved objects
        save_values = Activite.objects.create(
            code=code,
            nom=nom,
            idstructure=structure,  # Assign the Structure instance directly
            idaction=action,        # Assign the Action instance directly (or None)
            idrang=rang,           # Assign the Rang instance directly
            justification=justification,
            objectif='Aucun',
            prio=True,
            etat=True,
            partisprenantes=True,
            autreconcerne=True,
            cumulextrants=True,
            responsables=True,
            cumulindicateurs=True,
            date_enregistre='2023-03-10',
            derniere_modif='2023-03-10'
        )

        # Get the ID of the created instance (automatically assigned)
        activite_id = save_values.idactivite

        print(f"Nouvelle activité créée avec ID: {activite_id}")

        return redirect('/tache/')