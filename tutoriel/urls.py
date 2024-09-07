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
    path('users/',views.users,name='users')

 
    

















 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
