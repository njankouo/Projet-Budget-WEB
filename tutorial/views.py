from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from tutorial.forms import TacheForm
from tutorial.models import Tache
# Create your views here.
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import check_password  # Importez check_password
import io
from django.http import HttpResponse
from django.http import FileResponse
import os
from django.contrib.auth.hashers import make_password  
def Home(request):
   
    template="../website/authentification/login.html"
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
            code = request.POST['code']
            nom = request.POST['nom']  
            libelle = request.POST['libelle']  
            indicateur = request.POST['indicateur']  
            print(f"Nom: {nom}, Libelle: {libelle}, Indicateur: {indicateur}")  

            save_sousprogramme = Sousprogramme.objects.create(code=code,nom=nom, libelleobjectif=libelle, libelleindicateur=indicateur)  
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
            code= request.POST['code']
            nom = request.POST['nom']
            indicateur = request.POST['indicateur']
            objectif = request.POST['objectif']
            sous_programme_id = request.POST['sous_programme']

            # Récupérer l'instance de Sousprogramme
            sous_programme_instance = Sousprogramme.objects.get(id=sous_programme_id)
            

            # Créer l'activité avec l'instance de Sousprogramme
            save_activite = Activite.objects.create(
                code = code,
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
    operation_p = OperationDetail.objects.all()
    structure= Structure.objects.all()
    
    context={'operation_p':operation_p,'sourcefinancement':sourcefinancement,'typefinancement':typefinancement,'risque':risque,'sousprogramme':sousprogramme,'structure':structure,'operation':operation}
  
    template = '../website/operations_list.html'
    return render(request,template,context)
def configurations(request):
    annee = Annee.objects.all()
    nature =Naturetache.objects.all()
    source = Sourcefinacement.objects.all()
    type= Typefinancement.objects.all()
    risque =Risque.objects.all()
    prestataire = Societe.objects.all()
    context={'annee':annee,'nature':nature,'source':source,'type':type,'risque':risque,'prestataire':prestataire}
    template='../website/configurations.html'
    return render(request,template,context)
def add_annee(request):
    if request.method == 'POST':
        try:

         
            nom = request.POST['nom']
            etat = request.POST['etat']
            code= request.POST['code']
            save_annee = Annee.objects.create(nom=nom,etat=etat,code=code)
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
            type_financement = request.POST['type_financement']
            instance_type_financement= Typefinancement.objects.get(id=int(type_financement))
            save_nature_tache=Naturetache.objects.create(nom=nom,idtypefinancement=instance_type_financement)
            
            save_nature_tache.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/configurations/')
        except Exception as e:
            messages.error(request,"Erreur Survenue L'ors de L'enregistrement")
            return redirect('/configurations/')
    return redirect('/configurations/')
from django.contrib.auth.decorators import login_required
# @login_required(login_url = '/')  # Décorateur pour restreindre l'accès aux utilisateurs connectés
def dashboard(request):
    template = '../website/master.html'
    boncommande = Boncommande.objects.count()
    ligneboncommande = Ligneboncommande.objects.count()
    context = {'boncommande': boncommande, 'ligneboncommande': ligneboncommande}
    return render(request, template, context)
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
            # nature = request.POST['nature']
            # instance_nature = Naturetache.objects.get(id=int(nature))
            save_type_financement = Typefinancement.objects.create(nom=nom,etat=etat)
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
            sourcefinancement_ids = request.POST.getlist('sourcefinancement[]')  
            risque = request.POST['risque']  
            indicateur = request.POST['indicateur']  
            resultat = request.POST['resultat']  
            structure = request.POST['structure']

            if not sourcefinancement_ids:  # Vérifie si la liste est vide
                messages.error(request, "Aucune source de financement sélectionnée.")
                return redirect('/operations/')

            # Récupération des instances  
            instance_sous_programme = Sousprogramme.objects.get(id=int(sous_programme))  
            instance_activite = Activite.objects.get(id=int(activite))  
            instance_tache = Tache.objects.get(id=int(tache))  
            instance_type_financement = Typefinancement.objects.get(id=int(type_financement))  
            instance_risque = Risque.objects.get(id=int(risque))  
            instance_structure = Structure.objects.get(id=int(structure))

            # Log instances  
            print("Instances retrieved: ", instance_sous_programme, instance_activite, instance_tache, instance_type_financement, instance_risque)  

            # Création de l'opération  
            saveoperations = Operation.objects.create(  
                nom=nom,  
                idsousprogramme=instance_sous_programme,  
                idactivite=instance_activite,  
                idtache=instance_tache,  
                idtypefinancement=instance_type_financement,  
                idrisque=instance_risque,  
                indicateurspoursuivis=indicateur,  
                indicateurresult=resultat,
                idstructure=instance_structure  
            )  

            # Ajout des sources de financement à l'opération
            for source_id in sourcefinancement_ids:
                source = Sourcefinacement.objects.get(id=int(source_id))
                saveoperations.idsourcefinancement.add(source)  # Ajouter chaque source

            messages.success(request, 'Enregistrement réussi')  
            return redirect('/operations/')  
        
        except Exception as e:  
            print("An error occurred:", str(e))  
            messages.error(request, "Erreur lors de l'enregistrement.")  
            return redirect('/operations/')  

    return redirect('/operations/')

from django.shortcuts import render, get_object_or_404  
from django.db.models import Sum  
def operation_paragraphe(request,id):
    operation=Operation.objects.get(id=int(id))
    operation_source_financement=operation.idsourcefinancement.all()
    annee = Annee.objects.all()
    paragraphe=Paragraphe.objects.all()
    operation_detail = OperationDetail.objects.all()
   
    somme_montants = OperationDetail.objects.filter(idoperation=operation).aggregate(Sum('montant'))  

    # Calculer le montant total (avec gestion de valeurs nulles)  
    montant_total = somme_montants['montant__sum'] if somme_montants['montant__sum'] is not None else 0  

   
    template ='../website/operation_view.html'
    context={'montant_total': montant_total,'operation_detail':operation_detail,'operation':operation,'operation_source_financement':operation_source_financement,'annee':annee,'paragraphe':paragraphe}



    return render(request,template,context)

def delete_operation(request,id):
    operation=Operation.objects.get(id=int(id))
    operation.delete()
    messages.success(request,'Operation Retire Avec Succes')
    return redirect('/operations/')

def users(request):
    users=Utilisateur.objects.order_by('-id')
   
    context={
        'users':users,
        
    }
    template = '../website/authentification/register.html'
    return render(request,template,context)

def rubrique(request):
    template = '../website/rubrique.html'
    rubrique = Rubrique.objects.all()
    sous_rubrique= Sousrubrique.objects.all()
    context ={'rubrique':rubrique,'sous_rubrique':sous_rubrique}
    return render(request,template,context)

def sous_rubrique(request):
    template = '../website/sous_rubrique.html'
    sous_rubrique= Sousrubrique.objects.all()
    context={'sous_rubrique':sous_rubrique}
    return render(request,template,context)

def references(request):
    template = '../website/references.html'
    rubrique = Rubrique.objects.all()
    sous_rubrique= Sousrubrique.objects.all()
    reference = Elementcout.objects.all()
    context ={'rubrique':rubrique,'sous_rubrique':sous_rubrique,'reference':reference}
    return render(request,template,context)

def add_rubrique(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            save_rubrique = Rubrique.objects.create(nom=nom)

            save_rubrique.save()
            messages.success(request,'Enregistrement Effectue')
            return redirect('/rubrique/')
        except Exception as e:
            messages.error(request,'une erreur est survenue')
            return redirect('/rubrique/')
    return redirect('/rubrique/')

def add_sous_rubrique(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            rubrique = request.POST['rubrique']
            instance_rubrique = Rubrique.objects.get(id= int(rubrique))
            save_rubrique = Sousrubrique.objects.create(nom=nom,idrubrique=instance_rubrique)

            save_rubrique.save()
            messages.success(request,'Enregistrement Effectue')
            return redirect('/sous_rubrique/')
        except Exception as e:
            messages.error(request,'une erreur est survenue')
            return redirect('/sous_rubrique/')
    return redirect('/sous_rubrique/')

def search_sous_rubrique(request):
    selected_id = request.GET.get('id')
    
    # Vérifiez si l'ID est valide
    if not selected_id:
        return JsonResponse({'error': 'ID non fourni'}, status=400)
    
    try:
        sous_rubrique = Sousrubrique.objects.filter(idrubrique=selected_id).values('id', 'nom')
        return JsonResponse(list(sous_rubrique), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
import random  

def generate_unique_code():  
    # Générer une liste de chiffres de 0 à 9  
    digits = list(range(10))  
    # Mélanger les chiffres  
    random.shuffle(digits)  
    
    # S'assurer que nous avons au moins 8 chiffres uniques  
    unique_digits = digits[:8]  
    
    # Regrouper les chiffres en trois groupes  
    groups = [  
        ''.join(str(digit) for digit in unique_digits[i:i+3])  
        for i in range(0, len(unique_digits), 3)  
    ]  
    
    # Convertir les groupes en chaîne séparée par des tirets  
    code = '-'.join(groups)  
    return code   
def add_reference(request):
    if request.method == 'POST':
        try:

            libelle = request.POST['libelle']
            cu = request.POST['cu']
            rubrique = request.POST['rubrique']
            sous_rubrique = request.POST['sous_rubrique']
            conditionnement = request.POST['conditionnement']
            instance_rubrique = Rubrique.objects.get(id=int(rubrique))
            instance_sous_rubrique = Sousrubrique.objects.get(id=int(sous_rubrique))
           
            concatene=concatene = generate_unique_code()  
            save_element = Elementcout.objects.create(conditionnement=conditionnement,code=concatene,nom=libelle,prixunitaire=cu,idrubriquemercurial=instance_rubrique,idsousrubriquemercurial=instance_sous_rubrique)
            save_element.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/references/')
        except Exception as e:
            messages.error(request,f'Une Erreur est Survenue: {e}')
            return redirect('/references/')
    return redirect('/references/')

def commandes(request):
    template = '../website/commande.html'
    return render(request,template)


def configurations_tva(request):
    template = '../website/tva.html'
    tva = Tva.objects.all()
    context={'tva':tva}
    return render(request,template,context)

def configurations_ir(request):
    template = '../website/ir.html'
    ir=Ir.objects.all()
    context={'ir':ir}
    return render(request,template,context)


def add_tva(request):
    if request.method == 'POST':
        try:
            nom= request.POST['nom']

            save_tva = Tva.objects.create(nom=nom)
            save_tva.save()

            messages.success(request,'Enregistrement effectuee')

            return redirect('/configurations_tva/')
        except Exception as e:
            messages.error(request,f'Erreur survenue:{e}')

            return redirect('/configurations_tva/')
    return redirect('/configurations_tva/')



def add_ir(request):
    if request.method == 'POST':
        try:
            nom= request.POST['nom']

            save_tva = Ir.objects.create(nom=nom)
            save_tva.save()

            messages.success(request,'Enregistrement effectuee')

            return redirect('/configurations_tva/')
        except Exception as e:
            messages.error(request,'Erreur survenue')

            return redirect('/configurations_tva/')
    return redirect('/configurations_tva/')


def article(request):
    template = '../website/article.html'
    article=Article.objects.all()
    context={'article':article}
    return render(request,template,context)

def secteur(request):
    template = '../website/secteur.html'
    secteur=Secteur.objects.all()
    context={'secteur':secteur}
    return render(request,template,context)

def add_secteur(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']

            save_secteur = Secteur.objects.create(nom=nom)
            messages.success(request,'Enregistrement Reussi')
            return redirect('/secteur/')
        except Exception as e:
            messages.error(request,'Erreur Survenue')
            return redirect('/secteur/')
    return redirect('/secteur/')

def add_sous_secteur(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            secteur = request.POST['secteur']
            instance_secteur=Secteur.objects.get(id = int(secteur))
            print(nom)
            save_secteur = Soussecteur.objects.create(nom=nom,idsecteur=instance_secteur)
            messages.success(request,'Enregistrement Reussi')
            return redirect('/secteur/')
        except Exception as e:
            messages.error(request,'Erreur Survenue')
            return redirect('/secteur/')
    return redirect('/secteur/')

def sous_secteur(request):
    template ='../website/sous_secteur.html'
    sous_secteur=Soussecteur.objects.all()
    context={'sous_secteur':sous_secteur}
    return render(request,template,context)



def generate_code():  
    # Générer une liste de chiffres de 0 à 9  
    digits = list(range(10))  
    # Mélanger les chiffres  
    random.shuffle(digits)  
    
    # S'assurer que nous avons au moins 8 chiffres uniques  
    unique_digits = digits[:9]  
    
    # Regrouper les chiffres en trois groupes  
    groups = [  
        ''.join(str(digit) for digit in unique_digits[i:i+3])  
        for i in range(0, len(unique_digits), 3)  
    ]  
    
    # Convertir les groupes en chaîne séparée par des tirets  
    code = '-'.join(groups)  
    return code 
def add_article(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            code = request.POST['code']
            print(nom)
            save_article = Article.objects.create(nom=nom,code=code)
            messages.success(request,'Enregistrement Reussi')
            return redirect('/article/')
        except Exception as e:
            messages.error(request,'Erreur Survenue')
            return redirect('/article/')
    return redirect('/article/')

def generate_code_section():  
    # Générer une liste de chiffres de 0 à 9  
    digits = list(range(8))  
    # Mélanger les chiffres  
    random.shuffle(digits)  
    
    # S'assurer que nous avons au moins 8 chiffres uniques  
    unique_digits = digits[:8]  
    
    # Regrouper les chiffres en trois groupes  
    groups = [  
        ''.join(str(digit) for digit in unique_digits[i:i+4])  
        for i in range(0, len(unique_digits), 4)  
    ]  
    
    # Convertir les groupes en chaîne séparée par des tirets  
    code = '-'.join(groups)  
    return code 
def add_section(request):
    if request.method == 'POST':
        try:
            nom = request.POST['nom']
            article = request.POST['article']
            instance_article=Article.objects.get(id=int(article))
            code=request.POST['code']
            print(nom)
            save_section = Section.objects.create(nom=nom,idarticle=instance_article,code=code)
            messages.success(request,'Enregistrement Reussi')
            return redirect('/article/')
        except Exception as e:
            messages.error(request,'Erreur Survenue')
            return redirect('/article/')
    return redirect('/article/')

def section(request):
    template = '../website/section.html'
    section = Section.objects.all()
    context={'section':section}
    return render(request,template,context)


def paragraphe(request):
    template = '../website/paragraphe.html'
    article = Article.objects.all()
    paragraphe =Paragraphe.objects.all()
    
    context={'article':article,'paragraphe':paragraphe}
  
    return render(request,template,context)

def search_section(request):
    selected_id = request.GET.get('id')
    
    # Vérifiez si l'ID est valide
    if not selected_id:
        return JsonResponse({'error': 'ID non fourni'}, status=400)
    
    try:
        articles = Section.objects.filter(idarticle=selected_id).values('id', 'nom')
        return JsonResponse(list(articles), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def add_paragraphe(request):
    if request.method == 'POST':
        try:
            code = request.POST['code']
            nom = request.POST['nom']
            secteur = request.POST['secteur']
            article = request.POST['article']
            instance_secteur = Section.objects.get(id=int(secteur))
            instance_article= Article.objects.get(id=int(article))
          
            save_paragraphe=Paragraphe.objects.create(code=code,nom=nom,idsection=instance_secteur,idarticle=instance_article)
            save_paragraphe.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/paragraphe/')
        except Exception as e:
            print(f'erreur: {e}')
            messages.error(request,f'Une Erreur est Survenue: {e}')
            return redirect('paragraphe')
    return redirect('/paragraphe/')


def add_prestataire(request):
    if request.method == 'POST':
        try:
            nom= request.POST['nom']
            email = request.POST['email']
            tel= request.POST['tel']
            banque = request.POST['banque']
            swift = request.POST['swift']
            pays = request.POST['pays']
            ville = request.POST['pays']

            registre =request.POST['registre']
            contribuable = request.POST['contribuable']
            cnps_number = request.POST['cnps_number']
            boite_postale = request.POST['boite_postale']
            localisation = request.POST['localisation']


            save_prestataire = Societe.objects.create(
            registre = registre,
            contribuable=contribuable,
            cnps_number = cnps_number,
            boite_postale = boite_postale,
            localisation =localisation,
            nom=nom,ad1=email,contact=tel,bqswift=swift,bqpays=pays,bqville=ville,bqnom=banque)
            save_prestataire.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/configurations/')
        except Exception as e:
            messages.error(request,f'Une Erreur Est Survenue')
            return redirect('/configurations/')
    return redirect('/configurations/')
from django.db.models import F  

def search_operations(request):  
   
    selected_id = request.GET.get('id')  
   
    
    if not selected_id:  
        return JsonResponse({'error': 'ID non fourni'}, status=400)  
    
    try:  
        selected_id = int(selected_id)  
        
        sous_programmes = Operation.objects.filter(id=selected_id).values(  
            'idsousprogramme',   
            'nom',   
            'idactivite',   
            'idtache',
            
        ).annotate(  
            sousprogramme_nom=F('idsousprogramme__nom'),  
            activite_nom=F('idactivite__nom'),  
            tache_nom=F('idtache__nom'),
            
        )
        
        if not sous_programmes:  
            return JsonResponse({'error': 'Aucune opération trouvée pour cet ID'}, status=404)  
        
        return JsonResponse(list(sous_programmes), safe=False)  
    
    except ValueError:  
        return JsonResponse({'error': 'ID invalide, doit être un nombre entier'}, status=400)  
    except Exception as e:  
        print(f"Erreur: {str(e)}")  # Affiche l'erreur dans les logs  
        return JsonResponse({'error': str(e)}, status=500)  
def add_commande(request):  
    if request.method == 'POST':  
        try:  
            societe = request.POST['societe']  
            institution = request.POST['institution']
            numero_commande = request.POST['numero_commande']  
            # operations = request.POST['operations']  
            # sous_programme = request.POST['sous_programme']  
            # activite = request.POST['activite']  
            # tache = request.POST['tache']  
            tva = request.POST['tva']  
            ir = request.POST['ir']  # Corrigé pour utiliser 'ir' au lieu de 'tva'  

            # Récupération des instances  
            instance_institution=Institution.objects.get(id=int(institution))
            instance_societe = Societe.objects.get(id=int(societe))  
            # instance_operation = Operation.objects.get(id=int(operations))  
            # instance_sous_programme = Sousprogramme.objects.get(id=int(sous_programme))  
            # instance_activite = Activite.objects.get(id=int(activite))  
            # instance_tache = Tache.objects.get(id=int(tache))  
            instance_tva = Tva.objects.get(id=int(tva))  # Correction ici  
            instance_ir = Ir.objects.get(id=int(ir))  # Correction ici  

            # Création de l'instance de Boncommande  
            save_commande = Boncommande(  
                code=numero_commande,  
                idsociete=instance_societe,  
                idinstitution=instance_institution,
                # idoperation=instance_operation,  
                # idsousprogramme=instance_sous_programme,  
                # idactivite=instance_activite,  
                # idtache=instance_tache,  
                idtva=instance_tva,  
                idir=instance_ir  
            )  
            save_commande.save()  

            messages.success(request, 'Enregistrement Réussi')  
            return redirect(request.META.get('HTTP_REFERER','/'))  
        except Exception as e:  
            messages.error(request, f'Une erreur est survenue: {e}')  
            print(f'erreur: {e}')  
            return redirect(request.META.get('HTTP_REFERER','/'))  
    return redirect(request.META.get('HTTP_REFERER','/'))  



def add_references(request, id, context_dict={}):
    # Récupérer tous les détails de la commande pour l'ID donné
    boncommandes = DetailBonCommande.objects.filter(idboncommande=int(id))
    lignecommande = Ligneboncommande.objects.filter(idboncommande=id)
    
    if boncommandes.exists():
        # Récupérer toutes les opérations liées à ces détails de commande
        operations_liees = []
        for boncommande in boncommandes:
            operations_liees.append(boncommande.idoperation)  # Assurez-vous que idoperation est le bon champ
            
    else:
        messages.info(request, "Vous n\'avez Pas Encore La Possibilite D\'ajouter Les Lignes De Commande")
        return redirect(request.META.get('HTTP_REFERER','/'))  # Redirigez vers une vue appropriée

    template = '../website/lignecommande.html'
    reference = Elementcout.objects.all()
    operation = Operation.objects.all()
    commande =Boncommande.objects.all()
    context = {
        'operations_liees': operations_liees,  # Passez toutes les opérations liées
        'boncommandes': boncommandes,
        'reference': reference,
        'operation': operation,
        'bon_commande_id': id,
        'lignecommande':lignecommande,
        'commande':commande
      
          # Gardez toutes les opérations disponibles si nécessaire
    }

    return render(request, template, context)
import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
def serve_qr_code(request):
    file_path = os.path.join(settings.BASE_DIR, '../website/pdf/qr_code.png')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='image/png')
    else:
        raise Http404("Image not found")
from django.template import loader
from io import BytesIO
from xhtml2pdf import pisa   
import io
from django.template.loader import get_template
from django.utils.translation import gettext as _
import num2words

from django.templatetags.static import static
def fiche_bon(request, id):
    template_path = "../website/pdf/fiche_bon.html"
    

    try:
        template = get_template(template_path)
    except TemplateDoesNotExist:
        print(f"Error: Template '{template_path}' not found.")
        return HttpResponse("Template not found.", status=404)

    # Fetch Boncommande data
    try:
        image_url = 'website/static/img/nasla.jpeg'
        boncommande = Boncommande.objects.get(id=int(id))
        ligneboncommande = Ligneboncommande.objects.filter(idboncommande=boncommande)
        detail_bon_commande=DetailBonCommande.objects.filter(idboncommande=boncommande)
        somme_montants = Ligneboncommande.objects.filter(idboncommande=id).aggregate(Sum('total'))


    # Calculer le montant total (avec gestion de valeurs nulles)  
        montant_total = somme_montants['total__sum'] if somme_montants['total__sum'] is not None else 0  
        montant_lettres = num2words.num2words(montant_total, lang='fr')  # Remplacer 'fr' par le code de la langue souhaitée

    except Boncommande.DoesNotExist:
        return HttpResponse("Boncommande not found.", status=404)

    # Prepare context
    context = {'image_url':image_url,'montant_lettres':montant_lettres,'montant_total':montant_total,'boncommande': boncommande,'ligneboncommande':ligneboncommande,'detail_bon_commande':detail_bon_commande}
     
    # Render the template with the context
    html = template.render(context)

    # Create a BytesIO object to hold the PDF content
    result = io.BytesIO()

    # Convert HTML to PDF using pisaDocument
    try:
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
        if pdf.err:
            return HttpResponse("Error generating PDF.", status=500)
        
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return HttpResponse("Error generating PDF.", status=500)

    return HttpResponse("No content generated.", status=204)

def search_cu(request):
    selected_id = request.GET.get('id')
    
    # Vérifiez si l'ID est valide
    if not selected_id:
        return JsonResponse({'error': 'ID non fourni'}, status=400)
    
    try:
        cus = Elementcout.objects.filter(id=selected_id).values('id', 'prixunitaire')
        return JsonResponse(list(cus), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def add_ligne_commande(request):  
    if request.method == 'POST':  
        try:  
            code = request.POST['code']  
            reference = request.POST['reference']  
            cu = float(request.POST['cu'])  # Assurez-vous que c'est un float  
            qte = int(request.POST['qte'])   # Assurez-vous que c'est un int  
            prixT = float(request.POST['prixT'])  # Assurez-vous que c'est un float  
            montant = float(request.POST['montant'])  # Assurez-vous que c'est un float  
            paragraphe = request.POST.get('paragraphe', '')  
            operation = request.POST.get('operation', '')  
            annee = request.POST.get('annee', '')  

            # Vérifiez si les instances correspondantes existent  
            instance_element = Elementcout.objects.get(id=int(reference))  
            instance_code = Boncommande.objects.get(id=int(code))  
            instance_paragraphe = Paragraphe.objects.get(id=int(paragraphe))  
            instance_operation = Operation.objects.get(id=int(operation))  
            instance_annee = Annee.objects.get(id=int(annee))  

            if montant < prixT:  
                messages.info(request, 'Cette référence ne peut être ajoutée car le montant engagé est inférieur au prix total.')  
            else:  
                montant_paragraphe = montant - prixT  
                verified_operation_details = OperationDetail.objects.filter(  
                    idoperation=instance_operation,  
                    idparagraphe=instance_paragraphe,  
                    idannee=instance_annee  
                )  

                if verified_operation_details.exists():  
                    operation_detail = verified_operation_details.first()  # Récupérer la première instance correspondant à la requête  
                    operation_detail.montant = montant_paragraphe  # Mettre à jour le montant  
                    operation_detail.save()  # Enregistrer la modification  

                    # Créer la ligne de commande  
                    save_ligne_commande = Ligneboncommande.objects.create(  
                        prixunitaire=cu,  
                        quantite=qte,  
                        total=prixT,  
                        idelementcout=instance_element,  
                        idboncommande=instance_code  
                    )  
                    save_ligne_commande.save()  
                    messages.success(request, 'Enregistrement réussi.')  
                else:  
                    messages.warning(request, 'Les détails de l\'opération vérifiée n\'existent pas.')  

            # Redirection vers l'URL d'origine  
            return redirect(request.META.get('HTTP_REFERER', '/'))  
        except KeyError as ke:  
            messages.error(request, f'Erreur: Champ manquant - {str(ke)}')  
            return redirect(request.META.get('HTTP_REFERER', '/'))  
        except Elementcout.DoesNotExist:  
            messages.error(request, f'Erreur: Élément de coût avec id {reference} non trouvé.')  
            return redirect(request.META.get('HTTP_REFERER', '/'))  
        except Boncommande.DoesNotExist:  
            messages.error(request, f'Erreur: Bon de commande avec id {code} non trouvé.')  
            return redirect(request.META.get('HTTP_REFERER', '/'))  
        except ValueError as ve:  
            messages.error(request, f'Erreur: Vérifiez les valeurs entrées. - {str(ve)}')  
            return redirect(request.META.get('HTTP_REFERER', '/'))  
        except Exception as e:  
            messages.error(request, f'Erreur: {str(e)}')  
            return redirect(request.META.get('HTTP_REFERER', '/'))  
    else:  
        # Gérer le cas où la méthode n'est pas POST  
        return redirect(request.META.get('HTTP_REFERER', '/'))  
def delete_commande(request, id):  
    # Récupérer l'instance de Ligneboncommande ou renvoyer une 404 si non trouvée  
    lignecommande = get_object_or_404(Ligneboncommande, id=id)  
    
    # Supprimer l'instance  
    lignecommande.delete()  
    
    # Définir un message de succès  
    messages.success(request, 'Commande retirée avec succès.')  
    
    # Rediriger vers la même page
    return redirect(request.META.get('HTTP_REFERER'))  # Redirection vers la page d'origine

def search_activities(request):
    selected_id = request.GET.get('id')
    
    # Vérifiez si l'ID est valide
    if not selected_id:
        return JsonResponse({'error': 'ID non fourni'}, status=400)
    
    try:
        activite = Activite.objects.filter(idsousprogramme=selected_id).values('id', 'nom')
        return JsonResponse(list(activite), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def engagements(request):
    template = '../website/engagement.html'
   
    tva =Tva.objects.all()
    ir=Ir.objects.all()
    institution = Institution.objects.all()
    societe=Societe.objects.all()

    boncommande =Boncommande.objects.filter(status__in=[0,1])
    context={'tva':tva,'ir':ir,'boncommande':boncommande,'institution':institution,'societe':societe}

    return render(request,template,context)


def paragraphe_operation(request):  
    if request.method == 'POST':  
        try:  
            # Récupération des données du formulaire  
            operation_id = int(request.POST['operation'])  
            paragraphe_id = int(request.POST['paragraphe'])  
            annee_id = int(request.POST['annee'])  
            montant = float(request.POST['montant'])   

            # Récupération des instances correspondantes  
            instance_annee = Annee.objects.get(id=annee_id)  
            instance_paragraphe = Paragraphe.objects.get(id=paragraphe_id)  
            instance_operation = Operation.objects.get(id=operation_id)  

            # Vérification des détails d'opération existants  
            existing_details = OperationDetail.objects.filter(  
                idoperation=instance_operation,  
                idannee=instance_annee,  
                idparagraphe=instance_paragraphe  
            )  

           
            if existing_details.exists():  
                # Si des détails existent, mise à jour du montant  
                for existing_detail in existing_details:  
                    existing_detail.montant += montant  
                    existing_detail.save()  
                messages.success(request, 'Montant mis à jour avec succès')  
            else:  
                # Création d'un nouvel enregistrement  
                OperationDetail.objects.create(  
                    idoperation=instance_operation,  
                    idannee=instance_annee,  
                    idparagraphe=instance_paragraphe,  
                    montant=montant  
                )  
                messages.success(request, 'Enregistrement réussi')  

        except Annee.DoesNotExist:  
            messages.error(request, 'L\'année sélectionnée n\'existe pas.')  
        except Paragraphe.DoesNotExist:  
            messages.error(request, 'Le paragraphe sélectionné n\'existe pas.')  
        except Operation.DoesNotExist:  
            messages.error(request, 'L\'opération sélectionnée n\'existe pas.')  
        except ValueError:  
            messages.error(request, 'Veuillez entrer un montant valide.')  
        except Exception as e:  
            messages.error(request, f'Erreur: {str(e)}')  

    # Rediriger vers la page précédente  
    return redirect(request.META.get('HTTP_REFERER', '/'))  

def delete_paragraphe_operation(request,id):
    operation_paragraphe = OperationDetail.objects.get(id=int(id))
    operation_paragraphe.delete()
    messages.success(request,"Paragraphe retire de l\'operation")
    return redirect(request.META.get('HTTP_REFERER','/'))

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password  # Use Django's password hashing
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password  

def add_user(request):  
    if request.method == 'POST':  
        try:  
            nom = request.POST['nom']  
            prenom = request.POST['prenom']  
            email = request.POST['email'].lower()  # Normalise l'email  
            password = request.POST['password']  
            re_password = request.POST['re_password']  
            sexe = request.POST['sexe']  
            matricule = request.POST.get('matricule','')
            grade= request.POST.get('grade','')
            photo = request.FILES.get('photo')  # Utilisez get() pour gérer un fichier photo optionnel  

            # Vérifiez si l'utilisateur existe déjà  
            if Utilisateur.objects.filter(email=email).exists():  
                messages.error(request, 'Un utilisateur avec cet e-mail existe déjà.')  
                return redirect(request.META.get('HTTP_REFERER', '/'))  

            # Validez la correspondance des mots de passe  
            if password != re_password:  
                messages.error(request, 'Les mots de passe ne correspondent pas.')  
                return redirect(request.META.get('HTTP_REFERER', '/'))  

            # Hachage sécurisé du mot de passe  
            hashed_password = make_password(password)  

            # Création de l'utilisateur  
            user = Utilisateur.objects.create(  
                nom=nom,  
                prenom=prenom,  
                email=email,  
                password=hashed_password,  
                sexe=sexe,  
                photo=photo,  
                matricule= matricule,
                grade=grade
            )  

            # Message de succès  
            messages.success(request, 'Utilisateur créé avec succès.')  
            return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirection vers la page précédente  

        except Exception as e:  
            messages.error(request, f'Une erreur est survenue : {e}')  
            print(f'Une erreur est survenue : {e}')  # Journalisez le message d'erreur  

    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirection par défaut  

from django.utils import timezone



def user_login(request):  
    if request.method == 'POST':  
        email = request.POST.get('email', '').strip().lower()  
        password = request.POST.get('password', '').strip() 
        
        users = Utilisateur.objects.filter(email=email)  
        print(f'Email recherché : {email}')  
        print(f'Utilisateurs trouvés : {users}')  # Affiche les utilisateurs trouvés  
        
        if users.exists():  
            user = users.first()  
            print(f'Utilisateur trouvé : {user}, Mot de passe haché : {user.password}, Email : {user.email}')  
           
            # Vérifiez si le mot de passe est correct  
            if check_password(password, user.password):  
                user.last_login = timezone.now()  
                user.save()  
                login(request, user)  
                messages.success(request, 'Connexion réussie.')  
                return redirect('/dashboard/')  
              
            else:  
                print('Mot de passe incorrect.')  # Log pour le mot de passe incorrect  
                messages.error(request, 'Identifiants invalides. Veuillez réessayer.')  
        else:  
            print('Aucun utilisateur trouvé avec cet email.')  # Log si aucun utilisateur n'est trouvé  
            messages.error(request, 'Identifiants invalides. Veuillez réessayer.')  

    return render(request, '../website/authentification/login.html')
def search_paragraphe(request):  
    selected_id = request.GET.get('id')  

    # Validez que l'ID est fourni et qu'il est numérique  
    if not selected_id or not selected_id.isdigit():  
        return JsonResponse({'error': 'ID non valide'}, status=400)  

    selected_id = int(selected_id)  # Convertir en entier pour le filtrage  
    
    try:  
        # Requête pour obtenir les détails de l'opération, incluant le nom du paragraphe lié, en évitant les doublons
        paragraphs = OperationDetail.objects.filter(idoperation=selected_id) \
            .select_related('idparagraphe') \
            .values('idparagraphe__id', 'idparagraphe__nom') \
            .distinct()  # Ajout de distinct() pour éviter les doublons

        result = [  
            {  
                'idparagraphe': detail['idparagraphe__id'],  
                'nom': detail['idparagraphe__nom'],  
                'idoperation': selected_id  
            }  
            for detail in paragraphs  
        ]  

        return JsonResponse(result, safe=False)  # Retourner la liste des résultats  
    except Exception as e:  
        return JsonResponse({'error': str(e)}, status=500)


def institution(request):
    sous_secteur = Soussecteur.objects.all()
    institution= Institution.objects.all()
    context= {'sous_secteur':sous_secteur,'institution':institution}
    template = '../website/institution.html'
    return render(request,template,context)


def add_institution(request):
    if request.method == 'POST':
        try:
            code =request.POST['code']
            sigle = request.POST['sigle']
            nom= request.POST['nom']
            choix_strategique = request.POST['choix_strategique']
            sous_secteur = request.POST['sous_secteur']

            instance_sous_secteur=  Soussecteur.objects.get(id = int(sous_secteur))

            save_institution = Institution. objects.create(
                code=code,
                sigle= sigle,
                nom= nom,
                choixstrategique = choix_strategique,
                idsoussecteur = instance_sous_secteur
                
            )
            save_institution.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect(request.META.get('HTTP_REFERER','/'))
        except Exception as e:
            messages.error(request,f'une erreur est survenue: {e}')
    return redirect(request.META.get('HTTP_REFERER','/'))


def structure(request):
    template = '../website/structure.html'
    structure = Structure.objects.all()
    institution = Institution.objects.all()
    context ={'structure':structure,'institution':institution}
    return render(request,template,context)

def add_structure(request):
    if request.method == 'POST':
        try:
            code = request.POST['code']
            nom = request.POST['nom']
            sigle = request.POST['sigle']
            institution = request.POST['institution']
            arrete_creation = request.POST['arrete_creation']
            objectif_general = request.POST['objectif_general']
            objectif_specifique = request.POST['objectif_specifique']

            instance_institution=  Institution.objects.get(id = int(institution))
            save_structure = Structure.objects.create(
                code= code,
                nom = nom,
                sigle = sigle,
                idinstitution = instance_institution,
                arretecreation = arrete_creation,
                objectifgeneral = objectif_general,
                objectifspecifique = objectif_specifique
            )
            save_structure.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect(request.META.get('HTTP_REFERER','/'))
        except Exception as e:
            messages.error(request,f'Une Erreur Est Survenue')
        except Institution.DoesNotExist:
            messages.error(request,'Institution Inexistante')
    return redirect(request.META.get('HTTP_REFERER','/'))


def add_operations(request, id):  
    # Utiliser get_object_or_404 pour éviter les exceptions si le bon de commande n'existe pas  
    boncommande = get_object_or_404(Boncommande, id=int(id))  

    # Récupérer uniquement les détails associés à ce bon de commande  
    detail_bon_commande = DetailBonCommande.objects.filter(idboncommande_id=boncommande)  
    
    # Récupérer toutes les sociétés et opérations  
    prestataire = Societe.objects.all()  
    operation = Operation.objects.all()  

    context = {  
        'detail_bon_commande': detail_bon_commande,  # Renommer pour clarté  
        'boncommande': boncommande,  
        'operation': operation,  
        'prestataire': prestataire  
    }  

    template = '../website/detailcommande.html'  
    return render(request, template, context)  
def add_operation_commande(request):  
    if request.method == 'POST':  
        try:  
            operation_id = request.POST['operation']  
            sous_programme_id = request.POST['sous_programme']  
            activite_id = request.POST['activite']  
            tache_id = request.POST['tache']  
            paragraphes = request.POST.getlist('paragraphe', [])  
            # societe_id = request.POST['prestataire']  
            boncommande_id = request.POST['boncommande']  

            instance_operation = Operation.objects.get(id=int(operation_id))  
            instance_sous_programme = Sousprogramme.objects.get(id=int(sous_programme_id))  
            instance_activite = Activite.objects.get(id=int(activite_id))  
            instance_tache = Tache.objects.get(id=int(tache_id))  
            instance_boncommande = Boncommande.objects.get(id=int(boncommande_id))  
            # instance_societe = Societe.objects.get(id=int(societe_id))  
            print(paragraphes)
            # Création de détails pour chaque paragraphe  
            for paragraphe_id in paragraphes:  
                instance_paragraphe = Paragraphe.objects.get(id=int(paragraphe_id))  
                
                save_detail_boncommande = DetailBonCommande.objects.create(  
                    idoperation=instance_operation,  
                    idparagraphe=instance_paragraphe,  
                    idsousprogramme=instance_sous_programme,  
                    # idsociete=instance_societe,  
                    idtache=instance_tache,  
                    idactivite=instance_activite,  
                    idboncommande=instance_boncommande  
                )  
                save_detail_boncommande.save()  

            messages.success(request, 'Enregistrement Reussi')  
            return redirect(request.META.get('HTTP_REFERER', '/'))  
        
        except Operation.DoesNotExist:  
            messages.error(request, 'L\'opération spécifiée n\'existe pas.')  
        except Sousprogramme.DoesNotExist:  
            messages.error(request, 'Le sous-programme spécifié n\'existe pas.')  
        except Activite.DoesNotExist:  
            messages.error(request, 'L\'activité spécifiée n\'existe pas.')  
        except Tache.DoesNotExist:  
            messages.error(request, 'La tâche spécifiée n\'existe pas.')  
        except Paragraphe.DoesNotExist:  
            messages.error(request, 'Le paragraphe spécifié n\'existe pas.')  
        except Boncommande.DoesNotExist:  
            messages.error(request, 'Le bon de commande spécifié n\'existe pas.')  
        except Societe.DoesNotExist:  
            messages.error(request, 'La société spécifiée n\'existe pas.')  
        except Exception as e:  
            messages.error(request, f'une erreur est survenue: {e}')  

    return redirect(request.META.get('HTTP_REFERER', '/'))  
    

def search_operation(request):  
    selected_id = request.GET.get('id')  
    
    # Vérifiez si l'ID est valide  
    if not selected_id:  
        return JsonResponse({'error': 'ID non fourni'}, status=400)  
    
    try:  
        # Filtrer les opérations et joindre avec le modèle Paragraphe  
        operations = OperationDetail.objects.filter(idoperation_id=selected_id).select_related('idparagraphe')  
        
        results = [  
            {  
                'idparagraphe_id': operation.idparagraphe_id,  
                'nom_paragraphe': operation.idparagraphe.nom  # Récupérer le nom du paragraphe  
            }  
            for operation in operations  
        ]  
        
        # Vérifiez s'il y a des résultats  
        if not results:  
            return JsonResponse({'error': 'Aucune opération trouvée pour cet ID'}, status=404)  

        # Retourner les résultats au format JSON  
        return JsonResponse(results, safe=False)  
    
    except Exception as e:  
        # Gérer les exceptions générales  
        return JsonResponse({'error': str(e)}, status=500)  

def valid(request, id):
    if request.method == 'POST':
        try:
            boncommande = Boncommande.objects.get(id=int(id))
            boncommande.status = 1  # Assuming 1 represents "validated"
            boncommande.save()

            messages.success(request, 'Bon Commande Validé')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except Boncommande.DoesNotExist:
            messages.error(request, 'Bon Commande introuvable')
        except Exception as e:
            messages.error(request, f'Une erreur est survenue: {e}')

    return redirect(request.META.get('HTTP_REFERER', '/'))
def liquidation(request):
    template = '../website/liquidation.html'
    tva = Tva.objects.all()
    ir = Ir.objects.all()
    boncommande = Boncommande.objects.filter(status__in=[1, 2])
    context = {'tva': tva, 'ir': ir, 'boncommande': boncommande}
    return render(request, template, context)

def paiement(request):
    template = '../website/paiement.html'
    tva = Tva.objects.all()
    ir = Ir.objects.all()
    boncommande = Boncommande.objects.filter(status__in=[2, 3])
    context = {'tva': tva, 'ir': ir, 'boncommande': boncommande}
    return render(request, template, context)

def liquide(request,id):
    if request.method == 'POST':
        try:
            boncommande = Boncommande.objects.get(id=int(id))
            boncommande.status = 2  # Assuming 1 represents "validated"
            boncommande.save()

            messages.success(request, 'Bon Commande Liquidé')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except Boncommande.DoesNotExist:
            messages.error(request, 'Bon Commande introuvable')
        except Exception as e:
            messages.error(request, f'Une erreur est survenue: {e}')

def valid_paiement(request,id):
    if request.method == 'POST':
        try:
            boncommande = Boncommande.objects.get(id=int(id))
            boncommande.status = 3  # Assuming 1 represents "validated"
            boncommande.save()

            messages.success(request, 'Bon Commande Payé')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except Boncommande.DoesNotExist:
            messages.error(request, 'Bon Commande introuvable')
        except Exception as e:
            messages.error(request, f'Une erreur est survenue: {e}')


def search_annee(request):  
    operation_id = request.GET.get('operation_id')  
    paragraph_id = request.GET.get('paragraph_id')  
    
    try:  
        # Récupérer les années en fonction de l'opération et du paragraphe  
        annees = Annee.objects.filter(  
            operationdetail__idoperation_id=operation_id,  
            operationdetail__idparagraphe_id=paragraph_id  
        ).distinct()  # Utilise distinct() pour éviter les doublons  

        data = [{'idannee': annee.id, 'annee': annee.nom} for annee in annees]  # Renvoie le nom de l'année  
    except Exception as e:  
        data = []  

    return JsonResponse(data, safe=False)  


def search_montant(request):  
    operation_id = request.GET.get('operation_id')  
    paragraph_id = request.GET.get('paragraph_id')  
    year_id = request.GET.get('year_id')  

    try:  
        # Récupérer le montant en fonction de l'opération, du paragraphe, et de l'année  
        montant_detail = OperationDetail.objects.get(  
            idoperation_id=operation_id,  
            idparagraphe_id=paragraph_id,  
            idannee_id=year_id  
        )  
        montant = montant_detail.montant  
    except OperationDetail.DoesNotExist:  
        montant = None  # Aucun enregistrement correspondant trouvé  

    return JsonResponse({'montant': montant})