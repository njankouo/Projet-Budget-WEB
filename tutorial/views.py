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
    sourcefinancement= Sourcefinacement.objects.all()
    typefinancement = Typefinancement.objects.all()
    risque=Risque.objects.all()
    sousprogramme = Sousprogramme.objects.all()
    structure =Structure.objects.all()
    operation=Operation.objects.all()

    context={'sourcefinancement':sourcefinancement,'typefinancement':typefinancement,'risque':risque,'sousprogramme':sousprogramme,'structure':structure,'operation':operation}
  
    template = '../website/operations_list.html'
    return render(request,template,context)
def configurations(request):
    annee = Annee.objects.all()
    nature =Naturetache.objects.all()
    source = Sourcefinacement.objects.all()
    type= Typefinancement.objects.all()
    risque =Risque.objects.all()
    context={'annee':annee,'nature':nature,'source':source,'type':type,'risque':risque}
    template='../website/configurations.html'
    return render(request,template,context)
def add_annee(request):
    if request.method == 'POST':
        try:

         
            nom = request.POST['nom']
            etat = request.POST['etat']
            save_annee = Annee.objects.create(nom=nom,etat=etat)
            save_annee.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/configurations/')
        except Exception as e:
            messages.error(request,'Une Erreur Est Survenue')
            print(f"erreur:{e}")
            return redirect('/configurations/')
    return redirect('/configurations/')

def delete_annee(request,id):
    annee=Annee.objects.get(id=int(id))
    annee.delete()
    messages.success(request,'Annee Retire Avec Succes!')
    return redirect('/configurations/')
def delete_nature(request,id):
    delete_nature=Naturetache.objects.get(id=int(id))
    delete_nature.delete()
    return redirect('/configurations/')
def nature_tache(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            save_nature_tache=Naturetache.objects.create(nom=nom)
            save_nature_tache.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/configurations/')
        except Exception as e:
            messages.error(request,"Erreur Survenue L'ors de L'enregistrement")
            return redirect('/configurations/')
    return redirect('/configurations/')
def dashboard(request):
    template ='../website/master.html'
    return render(request,template)

def add_sources_financements(request):
    if request.method == 'POST':
        try:
            nom=request.POST['nom']
            etat = request.POST['etat']
            save_source_financement=Sourcefinacement.objects.create(nom=nom,etat=etat)
            save_Sous_programme.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/configurations/')
        except Exception as e:
            messages.error(request,"Erreur Survenue L'ors de L'enregistrement")
            return redirect('/configurations/')
    return redirect('/configurations/')

def delete_sources(request,id):
    sourcefinancement= Sourcefinacement.objects.get(id=int(id))
    sourcefinancement.delete()
    messages.success(request,'Source De Financement Retire ')
    return redirect('/configurations/')


def add_type_financements(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            etat= request.POST['etat']
            nature = request.POST['nature']
            instance_nature = Naturetache.objects.get(id=int(nature))
            save_type_financement = Typefinancement.objects.create(nom=nom,etat=etat,idnaturetache=instance_nature)
            save_type_financement.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/configurations/')
        except Exception as e:
            messages.error(request,f"Une Erreur:{e}")
            return redirect('/configurations/')
        except Naturetache.DoesNotExist:
            messages.error('La nature De La Tache Est Inexistante')
            return redirect('/configurations/')
    return redirect('/configurations/')

def delete_types(request,id):
    delete_type_financement= Typefinancement.objects.get(id=int(id))
    delete_type_financement.delete()
    messages.success(request,'Type De Financement Retire')
    return redirect('/configurations/')


def add_risque(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            etat = request.POST['etat']
            save_risque = Risque.objects.create(nom=nom,etat=etat)
            save_risque.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/configurations/')
        except Exception as e:
            messages.error(request,'Une Erreur Est Survenue')
            return redirect('/configurations/')
    return redirect('/configurations/')

def risques(request,id):
    delete_risque= Risque.objects.get(id=int(id))
    delete_risque.delete()
    messages.success(request,'Risque Retire Avec Succes')
    return redirect('/configurations/')
from django.http import JsonResponse

def search_activite(request):
    selected_id = request.GET.get('id')
    
    # Vérifiez si l'ID est valide
    if not selected_id:
        return JsonResponse({'error': 'ID non fourni'}, status=400)
    
    try:
        activites = Activite.objects.filter(idsousprogramme_id=selected_id).values('id', 'nom')
        return JsonResponse(list(activites), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def search_tache(request):
    selected_id = request.GET.get('id')
    
    # Vérifiez si l'ID est valide
    if not selected_id:
        return JsonResponse({'error': 'ID non fourni'}, status=400)
    
    try:
        taches = Tache.objects.filter(idactivite=selected_id).values('id', 'nom')
        return JsonResponse(list(taches), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




def add_operation(request):  
    if request.method == 'POST':  
        try:  
            # Log received data  
            print("Received POST data:", request.POST)  

            # Récupération des données du formulaire  
            nom = request.POST['nom']  
            sous_programme = request.POST['sousprogramme']  
            activite = request.POST['activite']  
            tache = request.POST['tache']  
            type_financement = request.POST['typefinancement']  
            sourcefinancement = request.POST['sourcefinancement']  
            risque = request.POST['risque']  
            indicateur = request.POST['indicateur']  
            resultat = request.POST['resultat']  

            # Récupération des instances  
            instance_sous_programme = Sousprogramme.objects.get(id=int(sous_programme))  
            instance_activite = Activite.objects.get(id=int(activite))  
            instance_tache = Tache.objects.get(id=int(tache))  
            instance_type_financement = Typefinancement.objects.get(id=int(type_financement))  
            instance_source_financement = Sourcefinacement.objects.get(id=int(sourcefinancement))  
            instance_risque = Risque.objects.get(id=int(risque))  

            # Log instances  
            print("Instances retrieved: ", instance_sous_programme, instance_activite, instance_tache, instance_type_financement, instance_source_financement, instance_risque)  

            # Création de l'opération  
            saveoperations = Operation.objects.create(  
                nom=nom,  
                idsousprogramme=instance_sous_programme,  
                idactivite=instance_activite,  
                idtache=instance_tache,  
                idtypefinancement=instance_type_financement,  
                idsourcefinancement=instance_source_financement,  
                idrisque=instance_risque,  
                indicateurspoursuivis=indicateur,  
                indicateurresult=resultat  
            )  

            messages.success(request, 'Enregistrement réussi')  
            return redirect('/operations/')  
        
        except Exception as e:  
            print("An error occurred:", str(e))  
            messages.error(request, "Erreur lors de l'enregistrement.")  
            return redirect('/operations/')  

    return redirect('/operations/')


def operation_paragraphe(request,id):
    operation=Operation.objects.get(id=int(id))
    template ='../website/operation_view.html'
    context={'operation':operation}
    return render(request,template,context)

def delete_operation(request,id):
    operation=Operation.objects.get(id=int(id))
    operation.delete()
    messages.success(request,'Operation Retire Avec Succes')
    return redirect('/operations/')