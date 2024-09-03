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
from tutorial.views import Task
from tutorial.views import Operation
from tutorial.views import list_taches

from tutorial import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('task', Task, name='task'),
 
   
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
 
    

















 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
