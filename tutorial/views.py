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
    prestataire = Societe.objects.all()
    context={'annee':annee,'nature':nature,'source':source,'type':type,'risque':risque,'prestataire':prestataire}
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
def dashboard(request):
    template ='../website/master.html'
    boncommande = Boncommande.objects.count()
    ligneboncommande = Ligneboncommande.objects.count()
    context={'boncommande':boncommande,'ligneboncommande':ligneboncommande}
    return render(request,template,context)

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

            if not sourcefinancement_ids:  # Vérifie si la liste est vide
                messages.error(request, "Aucune source de financement sélectionnée.")
                return redirect('/operations/')

            # Récupération des instances  
            instance_sous_programme = Sousprogramme.objects.get(id=int(sous_programme))  
            instance_activite = Activite.objects.get(id=int(activite))  
            instance_tache = Tache.objects.get(id=int(tache))  
            instance_type_financement = Typefinancement.objects.get(id=int(type_financement))  
            instance_risque = Risque.objects.get(id=int(risque))  

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
                indicateurresult=resultat  
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


def operation_paragraphe(request,id):
    operation=Operation.objects.get(id=int(id))
    operation_source_financement=operation.idsourcefinancement.all()
    template ='../website/operation_view.html'
    context={'operation':operation,'operation_source_financement':operation_source_financement}
    return render(request,template,context)

def delete_operation(request,id):
    operation=Operation.objects.get(id=int(id))
    operation.delete()
    messages.success(request,'Operation Retire Avec Succes')
    return redirect('/operations/')

def users(request):
    template = '../website/authentification/register.html'
    return render(request,template)

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
def add_references(request):
    if request.method == 'POST':
        try:

            libelle = request.POST['libelle']
            cu = request.POST['cu']
            rubrique = request.POST['rubrique']
            sous_rubrique = request.POST['sous_rubrique']
            instance_rubrique = Rubrique.objects.get(id=int(rubrique))
            instance_sous_rubrique = Sousrubrique.objects.get(id=int(sous_rubrique))
           
            concatene=concatene = generate_unique_code()  
            save_element = Elementcout.objects.create(code=concatene,nom=libelle,prixunitaire=cu,idrubriquemercurial=instance_rubrique,idsousrubriquemercurial=instance_sous_rubrique)
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
            code = generate_code()
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
            code=generate_code_section()
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
            nom = request.POST['nom']
            secteur = request.POST['secteur']
            article = request.POST['article']
            instance_secteur = Section.objects.get(id=int(secteur))
            instance_article= Article.objects.get(id=int(article))
          
            save_paragraphe=Paragraphe.objects.create(nom=nom,idsection=instance_secteur,idarticle=instance_article)
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
            save_prestataire = Societe.objects.create(nom=nom,ad1=email,contact=tel,bqswift=swift,bqpays=pays,bqville=ville,bqnom=banque)
            save_prestataire.save()
            messages.success(request,'Enregistrement Reussi')
            return redirect('/configurations/')
        except Exception as e:
            messages.error(request,f'Une Erreur Est Survenue')
            return redirect('/configurations/')
    return redirect('/configurations/')
from django.db.models import F  

def search_operations(request):  
    print("Requête reçue")  
    selected_id = request.GET.get('id')  
    print(f"ID sélectionné: {selected_id}")  
    
    if not selected_id:  
        return JsonResponse({'error': 'ID non fourni'}, status=400)  
    
    try:  
        selected_id = int(selected_id)  
        
        sous_programmes = Operation.objects.filter(id=selected_id).values(  
            'idsousprogramme',   
            'nom',   
            'idactivite',   
            'idtache'  
        ).annotate(  
            activite_nom=F('idactivite__nom'),  
            tache_nom=F('idtache__nom')  
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
            numero_commande = request.POST['numero_commande']  
            operations = request.POST['operations']  
            sous_programme = request.POST['sous_programme']  
            activite = request.POST['activite']  
            tache = request.POST['tache']  
            tva = request.POST['tva']  
            ir = request.POST['ir']  # Corrigé pour utiliser 'ir' au lieu de 'tva'  

            # Récupération des instances  
            instance_societe = Societe.objects.get(id=int(societe))  
            instance_operation = Operation.objects.get(id=int(operations))  
            instance_sous_programme = Sousprogramme.objects.get(id=int(sous_programme))  
            instance_activite = Activite.objects.get(id=int(activite))  
            instance_tache = Tache.objects.get(id=int(tache))  
            instance_tva = Tva.objects.get(id=int(tva))  # Correction ici  
            instance_ir = Ir.objects.get(id=int(ir))  # Correction ici  

            # Création de l'instance de Boncommande  
            save_commande = Boncommande(  
                code=numero_commande,  
                idsociete=instance_societe,  
                idoperation=instance_operation,  
                idsousprogramme=instance_sous_programme,  
                idactivite=instance_activite,  
                idtache=instance_tache,  
                idtva=instance_tva,  
                idir=instance_ir  
            )  
            save_commande.save()  

            messages.success(request, 'Enregistrement Réussi')  
            return redirect('/commandes/')  
        except Exception as e:  
            messages.error(request, f'Une erreur est survenue: {e}')  
            print(f'erreur: {e}')  
            return redirect('/commandes/')  
    return redirect('/commandes/')  


def add_references(request,id, context_dict={}):
    boncommande =Boncommande.objects.get(id=int(id))
    template ='../website/lignecommande.html'
    reference = Elementcout.objects.all()

    ligneboncommande =Ligneboncommande.objects.all()
    
    context={'boncommande':boncommande,'reference':reference,'ligneboncommande':ligneboncommande}
  
    return render(request,template,context)
from django.template import loader
from io import BytesIO
from xhtml2pdf import pisa   
import io
from django.template.loader import get_template
def fiche_bon(request, id):
    template_path = "../website/pdf/fiche_bon.html"

    try:
        template = get_template(template_path)
    except TemplateDoesNotExist:
        print(f"Error: Template '{template_path}' not found.")
        return HttpResponse("Template not found.", status=404)

    # Fetch Boncommande data
    try:
        boncommande = Boncommande.objects.get(id=int(id))
    except Boncommande.DoesNotExist:
        return HttpResponse("Boncommande not found.", status=404)

    # Prepare context
    context = {'boncommande': boncommande}

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

def add_ligne_commande(request, id):  
    if request.method == 'POST':  
        try:  
            code = request.POST['code']  
            reference = request.POST['reference']  
            cu = request.POST['cu']  
            qte = request.POST['qte']  
            prixT = request.POST['prixT']  
            instance_element = Elementcout.objects.get(id=int(reference))  
            instance_code = Boncommande.objects.get(id=int(code))
            save_ligne_commande = Ligneboncommande.objects.create(  
                prixunitaire=cu,  
                quantite=qte,  
                total=prixT,  
                idelementcout=instance_element,  
                idboncommande=instance_code  
            )  
            save_ligne_commande.save()  
            messages.success(request, 'Enregistrement Réussi')  
            
            # Redirection vers l'URL avec l'ID de référence  
            return redirect(f'/add_references/{id}/')  
        except Exception as e:  
            messages.error(request, f'Erreur: {str(e)}')  
            return redirect(f'/add_references/{id}/')  # Redirige même en cas d'erreur  
    else:  
        # Gérer le cas où la méthode n'est pas POST  
        return redirect(f'/add_references/{reference_id}/')  


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
    prestataire = Societe.objects.all()
    operation = Operation.objects.all()
    tva =Tva.objects.all()
    ir=Ir.objects.all()
    boncommande =Boncommande.objects.all()
    context={'operation':operation,'prestataire':prestataire,'tva':tva,'ir':ir,'boncommande':boncommande}

    return render(request,template,context)