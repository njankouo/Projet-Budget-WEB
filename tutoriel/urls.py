"""
URL configuration for tutoriel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import  path
from tutorial.views import Home

from tutorial.views import Operation
from tutorial.views import list_taches

from tutorial import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    
 
   
 

    path('list_taches/', list_taches, name='list_taches'),
    path('delete_tache/<int:id>/',views.delete_tache,name="delete_tache"),
    path('tache/',views.tache,name="tache"),
    path('new_tache/',views.new_tache,name="new_tache"),
    path('sous_programme/',views.sous_programme,name='sous_programme'),
    path('add_sous_programme/',views.add_sous_programme,name='add_sous_programme'),
    path('save_Sous_programme/',views.save_Sous_programme,name='save_Sous_programme'),
    path('activites/',views.activites,name='activites'),
    path('add_activite/',views.add_activite,name='add_activite'),
    path('save_activity/',views.save_activity,name='save_activity'),
    path('users/',views.users,name='users'),
    path('save_taches/',views.save_taches,name='save_taches'),
    path('operations/',views.operations,name='operations'),
    path('configurations/',views.configurations,name='configurations'),
    path('add_annee/',views.add_annee,name='add_annee'),
    path('delete_annee/<int:id>/',views.delete_annee,name='delete_annee'),
    path('nature_tache/',views.nature_tache,name='nature_tache'),
    path('delete_nature/<int:id>/',views.delete_nature,name='delete_nature'),

    path('add_sources_financements/',views.add_sources_financements,name='add_sources_financements'),

    path('delete_sources/<int:id>/',views.delete_sources,name='delete_sources'),
    path('add_type_financements/',views.add_type_financements,name='add_type_financements'),
    path('delete_types/<int:id>/',views.delete_types,name='delete_types'),
    path('add_risque/',views.add_risque,name='add_risque'),
    path('risques/<int:id>/',views.risques,name='risques'),


    path('search_activite/',views.search_activite,name='search_activite'),

    path('search_tache/',views.search_tache,name='search_tache'),
    path('add_operation/',views.add_operation,name='add_operation'),

    path('operation_paragraphe/<int:id>/',views.operation_paragraphe,name='operation_paragraphe'),


    path('delete_operation/<int:id>/',views.delete_operation,name='delete_operation'),
    path('users/',views.users,name='users'),

    path('rubrique/',views.rubrique,name='rubrique'),
    path('sous_rubrique/',views.sous_rubrique,name='sous_rubrique'),
    path('references/',views.references,name='references'),

    path('add_rubrique/',views.add_rubrique,name='add_rubrique'),

    path('add_sous_rubrique/',views.add_sous_rubrique,name='add_sous_rubrique'),


    path('search_sous_rubrique/',views.search_sous_rubrique,name='search_sous_rubrique'),

    path('add_reference/',views.add_reference,name='add_reference'),

    path('commandes/',views.commandes,name='commandes'),
    path('configurations_tva/',views.configurations_tva,name='configurations_tva'),
    path('configurations_ir/',views.configurations_ir,name='configurations_ir'),

    path('add_tva/',views.add_tva,name='add_tva'),

    path('add_ir/',views.add_ir,name='add_ir'),
    path('secteur/',views.secteur,name='secteur'),
    path('article/',views.article,name='article'),
    path('add_secteur/',views.add_secteur,name='add_secteur'),

    path('add_sous_secteur/',views.add_sous_secteur,name='add_sous_secteur'),
    path('sous_secteur/',views.sous_secteur,name='sous_secteur'),
    path('add_article/',views.add_article,name='add_article'),

    path('add_section/',views.add_section,name='add_section'),

    path('section',views.section,name='section'),

    path('paragraphe/',views.paragraphe,name='paragraphe'),
 
    path('search_section/',views.search_section,name='search_section'),

    path('add_paragraphe/',views.add_paragraphe,name='add_paragraphe'),

    path('add_prestataire/',views.add_prestataire,name='add_prestataire'),

    path('search_operations/',views.search_operations,name='search_operations'),
    path('add_commande/',views.add_commande,name='add_commande'),

    path('add_references/<int:id>/',views.add_references,name='add_references'),
    path('fiche_bon/<int:id>/',views.fiche_bon,name='fiche_bon'),
    path('search_cu/',views.search_cu,name='search_cu'),
    path('add_ligne_commande/',views.add_ligne_commande,name='add_ligne_commande'),
    path('delete_commande/<int:id>/',views.delete_commande,name='delete_commande'),

    path('search_activities/',views.search_activities,name='search_activities'),
    path('engagements/',views.engagements,name='engagements'),

    path('paragraphes_operations/',views.paragraphe_operation,name='paragraphes_operations'),

    path('delete_paragraphe_operation/<int:id>/',views.delete_paragraphe_operation,name='delete_paragraphe_operation'),

    path('add_user/',views.add_user,name='add_user'),

    path('user_login/',views.user_login,name='user_login'),

    path('search_paragraphe/',views.search_paragraphe,name='search_paragraphe'),


    path('institution/',views.institution,name='institution'),

    path('add_institution/',views.add_institution,name='add_institution'),

    path('structure/',views.structure,name='structure'),

    path('add_structure/',views.add_structure,name='add_structure'),
    path('add_operations/<int:id>/',views.add_operations,name='add_operations'),

    path('add_operation_commande/',views.add_operation_commande,name='add_operation_commande'),

    path('search_operation/',views.search_operation,name='search_operation'),
    path('valid/<int:id>/',views.valid,name='valid')
,
    path('liquidation/',views.liquidation,name='liquidation'),
    path('paiement/',views.paiement,name='paiement'),
    path('liquide/<int:id>/',views.liquide,name='liquide'),
    path('valid_paiement/<int:id>/',views.valid_paiement,name='valid_paiement'),

    path('search_annee/',views.search_annee,name='search_annee'),
    path('search_montant/',views.search_montant,name='search_montant'),
    path('serve_qr_code/',views.serve_qr_code,name='serve_qr_code'),
    path('certificat/<int:id>/',views.certificat,name='certificat'),
    path('fiche/<int:id>/',views.fiche,name='fiche'),
    path('add_lettre_commande/',views.add_lettre_commande,name='add_lettre_commande'),

    path('add_operation_lettre/<int:id>/',views.add_operation_lettre,name='add_operation_lettre'),
    path('add_operation_lettre_commande/',views.add_operation_lettre_commande,name='add_operation_lettre_commande'),

    path('add_references_lettre/<int:id>/',views.add_references_lettre,name='add_references_lettre'),
    path('delete_sous_programme/<int:id>/',views.delete_sous_programme,name='delete_sous_programme'),
    path('edit_sousprogramme/<int:id>/',views.edit_sousprogramme,name='edit_sousprogramme')











 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
