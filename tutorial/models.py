from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password  # Use Django's password hashing

class Statutmatrimonial(models.Model):
    libelle=models.CharField(max_length=255, null=True)
    etat=models.CharField(max_length=255, null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'statutmatrimonial'  

    def __str__(self):
        return self.nom
    
class Risque(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'risque'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
class Typefinancement(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    # idnaturetache=models.ForeignKey(Naturetache, on_delete=models.CASCADE, null=True,blank=True, db_column='idnaturetache')
    class Meta:
        db_table = 'typefinancement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Naturetache(models.Model):
    nom=models.CharField(max_length=255,null=True)
    idtypefinancement = models.ForeignKey(Typefinancement,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'naturetache'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Sourcefinacement(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'sourcefinancement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom


class Frequence(models.Model):
    nom=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'frequence'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Basejuridique(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'basejuridique'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Axestrategique(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'axestrategique'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
   
class Rang(models.Model):
    nom=models.CharField(max_length=255,null=True)
    numero=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'rang'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
   

class Typedonnees(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'typedonnees'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
   

class Zone(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'zone'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Typeactivite(models.Model):
    nom=models.CharField(max_length=255,null=True)
    numero=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'typeactivite'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Niveaupyramide(models.Model):
    code=models.CharField(max_length=255,null=True)
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'niveaupyramide'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Rattachement(models.Model):
    nom=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'rattachement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
   
class Statstructure(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'statstructure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Typestructure(models.Model):
    nom=models.CharField(max_length=255,null=True)
    designation=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=2555,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'typestructure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Article(models.Model):
    code=models.CharField(max_length=255,null=True)
    nom= models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'article'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Typeimputation(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'typeimputation'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Composante(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'composante'  # Specify the exact table name you want

    def __str__(self):
        return self.nom


class Critere(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    poids=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'critere'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Unite(models.Model):
    nom=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'unite'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Menu_b(models.Model):
    nom=models.CharField(max_length=255,null=True)
    ressource=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'menu_b'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Rubrique(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'rubrique'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Reglage(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    valeur=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'reglage'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Parametres(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    valeur=models.CharField(max_length=255,null=True)
    min=models.CharField(max_length=255,null=True)
    max=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'parametres'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Secteur(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'secteur'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

   
class Pap(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'pap'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Parent(models.Model):
    nom = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'parent'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

    
class Continent(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'continent'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Pays(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    date_enregistre=models.CharField(max_length=255,null=True)
    drapeau=models.CharField(max_length=255,null=True)
    drapeau_relatif=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idcontinent=models.ForeignKey(Continent, on_delete=models.CASCADE, null=True,blank=True,db_column='idcontinent')
    class Meta:
        db_table = 'pays'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Region(models.Model):
    nom=models.CharField(max_length=255,null=True)
    superfiecie=models.CharField(max_length=255,null=True)
    population=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idpays=models.ForeignKey(Pays, on_delete=models.CASCADE, null=True,blank=True, db_column='idpays')
    class Meta:
        db_table = 'region'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Departement(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    # date_enregistre=models.CharField(null=True,blank=True)
    # derniere_modif=models.CharField(null=True,blank=True)
    idregion=models.ForeignKey(Region, on_delete=models.CASCADE, null=True,blank=True, db_column='idregion')
    class Meta:
        db_table = 'departement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Arrondissement(models.Model):
    nom=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    iddepartement=models.ForeignKey(Departement, on_delete=models.CASCADE, null=True,blank=True, db_column='iddepartement')
    class Meta:
        db_table = 'arrondissement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Ville(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idpays=models.ForeignKey(Pays, on_delete=models.CASCADE, null=True,blank=True, db_column='idpays')
    class Meta:
        db_table = 'ville'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Quartier(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idville=models.ForeignKey(Ville, on_delete=models.CASCADE, null=True,blank=True, db_column='idville')
    class Meta:
        db_table = 'quartier'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Rue(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistrement=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idquartier=models.ForeignKey(Quartier, on_delete=models.CASCADE, null=True,blank=True, db_column='idquartier')
    class Meta:
        db_table = 'rue'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Adresse(models.Model):
    contact=models.CharField(max_length=255,null=True)
    fax=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=255,null=True)
    bp=models.CharField(max_length=255,null=True)
    siteweb=models.CharField(max_length=255,null=True)
    idquartier=models.ForeignKey(Quartier, on_delete=models.CASCADE, null=True,blank=True, db_column='idquartier')
    idrue=models.ForeignKey(Rue, on_delete=models.CASCADE, null=True,blank=True, db_column='idrue')
    idville=models.ForeignKey(Ville, on_delete=models.CASCADE, null=True,blank=True, db_column='idville')
    class Meta:
        db_table = 'adresse'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
class Role(models.Model):
    NOM_ROLES={
        'SA':'SuperAdministrateur',
        'A':'Administrateur',
        'SU':'Simple Utilisateur'
    }
    nom=models.CharField(null=True,max_length=255,choices=NOM_ROLES)

    class META:
        db_table='role'
class Utilisateur(models.Model):
    grade = models.CharField(null=True,max_length=255)
    matricule= models.CharField(null=True,max_length=255)
    nom=models.CharField(max_length=255,null=True)
    prenom=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    sexe=models.IntegerField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    date_naissance=models.DateTimeField(null=True,blank=True)
    email=models.CharField(max_length=255,null=True)
    password = models.CharField(max_length=255,null=True)
    photo = models.FileField(null=True)
    telephone = models.IntegerField(null=True)
    last_login = models.DateTimeField(null=True, blank=True)  # Ajoutez ce champ
    idrole = models.ManyToManyField(Role,null=True)

    # idarrondissement=models.ForeignKey(Arrondissement, on_delete=models.CASCADE, null=True,blank=True, db_column='idarrondissement')
    # idstatut_matrimonial=models.ForeignKey(Statutmatrimonial, on_delete=models.CASCADE, null=True,blank=True, db_column='idstatut_matrimonial')
    # idpays=models.ForeignKey(Pays, on_delete=models.CASCADE, null=True,blank=True, db_column='idpays')
    # idadresse=models.ForeignKey(Adresse, on_delete=models.CASCADE, null=True,blank=True, db_column='idadresse')
    class Meta:
        db_table = 'utilisateur'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    def save(self, *args, **kwargs):
        if not self.pk:  # Si c'est un nouvel utilisateur
            self.password = make_password(self.password)  # Hachage du mot de passe
        super().save(*args, **kwargs)

class Compte(models.Model):
    login=models.CharField(max_length=255,null=True)
    mdp=models.CharField(max_length=255,null=True)
    langue=models.CharField(max_length=255,null=True)
    connexion=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    role=models.CharField(max_length=255,null=True)
    heure_denregistre=models.TimeField(null=True,blank=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idutilisateur=models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True,blank=True, db_column='idutilisateur')
    class Meta:
        db_table = 'compte'  # Specify the exact table name you want

    def __str__(self):
        return self.nom


class Nature_t(models.Model):
    nom=models.CharField(max_length=255,null=True)
    idnaturetache=models.ForeignKey(Naturetache, on_delete=models.CASCADE, null=True,blank=True, db_column='idnaturetache')
    class Meta:
        db_table = 'nature_t'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Bailleurfond(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idsourcefinancement=models.ForeignKey(Sourcefinacement, on_delete=models.CASCADE, null=True,blank=True, db_column='idsourcefinancement')
    class Meta:
        db_table = 'bailleurfond'  # Specify the exact table name you want

    def __str__(self):
        return self.nom



class Soussecteur(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idsecteur=models.ForeignKey(Secteur, on_delete=models.CASCADE, null=True,blank=True, db_column='idsecteur')
    class Meta:
        db_table = 'soussecteur'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Institution(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    choixstrategique=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    # date_enregistre=models.DateTimeField(null=True,blank=True)
    # derniere_modif=models.DateTimeField(null=True,blank=True)
    sigle=models.CharField(max_length=255,null=True)
    chapitre=models.CharField(max_length=255,null=True) 
    nom_en=models.CharField(max_length=255,null=True)
    idsoussecteur=models.ForeignKey(Soussecteur, on_delete=models.CASCADE, null=True,blank=True, db_column='idsoussecteur')
    class Meta:
        db_table = 'institution'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Pyramide(models.Model):
    nom=models.CharField(max_length=255,null=True)
    superficie=models.CharField(max_length=255,null=True)
    population=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idniveaupyramide=models.ForeignKey(Niveaupyramide, on_delete=models.CASCADE, null=True,blank=True, db_column='idniveaupyramide')
    class Meta:
        db_table = 'pyramide'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Statutstructure(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'statutstructure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Structure(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    sigle=models.CharField(max_length=255,null=True)
    arretecreation=models.CharField(max_length=255,null=True)
    designation=models.CharField(max_length=255,null=True)
    cordonex=models.CharField(max_length=255,null=True)
    cordoney=models.CharField(max_length=255,null=True)
    presentation=models.CharField(max_length=255,null=True)
    pap=models.CharField(max_length=255,null=True)
    actif=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    dateouverture=models.DateTimeField(null=True,blank=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    vision=models.CharField(max_length=255,null=True)
    axeintervention=models.CharField(max_length=255,null=True)
    objectifgeneral=models.CharField(max_length=255,null=True)
    objectifspecifique=models.CharField(max_length=255,null=True)
    # idarrondissement=models.ForeignKey(Arrondissement, on_delete=models.CASCADE, null=True,blank=True, db_column='idarrondissement')
    # idtypestructure=models.ForeignKey(Typestructure, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypestructure')
    # idadresse=models.ForeignKey(Adresse, on_delete=models.CASCADE, null=True,blank=True, db_column='idadresse')
    # iddepartement=models.ForeignKey(Departement, on_delete=models.CASCADE, null=True,blank=True, db_column='iddepartement')
    # idstatutstructure=models.ForeignKey(Statutstructure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstatutstructure')
    # idniveaupyramide=models.ForeignKey(Niveaupyramide, on_delete=models.CASCADE, null=True,blank=True, db_column='idniveaupyramide')
    # idpyramide=models.ForeignKey(Pyramide, on_delete=models.CASCADE, null=True,blank=True, db_column='idpyramide')
    # idregion=models.ForeignKey(Region, on_delete=models.CASCADE, null=True,blank=True, db_column='idregion')
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True,blank=True, db_column='idinstitution')
    # idrattachement=models.ForeignKey(Rattachement, on_delete=models.CASCADE, null=True,blank=True, db_column='idrattachement')
    class Meta:
        db_table = 'structure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Section(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    idarticle=models.ForeignKey(Article, on_delete=models.CASCADE, null=True,blank=True, db_column='idarticle')
    class Meta:
        db_table = 'section'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Periode(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    idfrequence=models.ForeignKey(Frequence, on_delete=models.CASCADE, null=True,blank=True, db_column='idfrequence')
    class Meta:
        db_table = 'periode'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Souscritere(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    detail=models.CharField(max_length=255,null=True)
    service=models.CharField(max_length=255,null=True)
    personel=models.CharField(max_length=255,null=True)
    idcomposante=models.ForeignKey(Composante, on_delete=models.CASCADE, null=True,blank=True, db_column='idcomposante')
    idcritere=models.ForeignKey(Critere, on_delete=models.CASCADE, null=True,blank=True, db_column='idcritere')
    class Meta:
        db_table = 'souscritere'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Sousprogramme(models.Model):
    code = models.CharField(null=True,max_length=255)
    nom=models.CharField(max_length=255,null=True)
    libelleobjectif=models.CharField(max_length=255,null=True)
    libelleindicateur=models.CharField(max_length=255,null=True)
    
    class Meta:
        db_table = 'sousprogramme'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Mission(models.Model):
    code=models.CharField(max_length=255,null=True)
    problemes=models.CharField(max_length=255,null=True)
    objectgeneral=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    objectspecifique=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    objectifs=models.CharField(max_length=255,null=True)
    objectifstrategique=models.CharField(max_length=255,null=True)
    nom=models.CharField(max_length=255,null=True)
    idniveaupyramide=models.ForeignKey(Niveaupyramide, on_delete=models.CASCADE, null=True,blank=True, db_column='idniveaupyramide')
    idbasejuridique=models.ForeignKey(Basejuridique, on_delete=models.CASCADE, null=True,blank=True, db_column='idbasejuridique')
    class Meta:
        db_table = 'mission'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Detailsc(models.Model):
    pointmax=models.CharField(max_length=255,null=True)
    detail=models.CharField(max_length=255,null=True)
    problemes=models.CharField(max_length=255,null=True)
    objectif=models.CharField(max_length=255,null=True)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idsouscritere=models.ForeignKey(Souscritere, on_delete=models.CASCADE, null=True,blank=True, db_column='idsouscritere')
    idmission=models.ForeignKey(Mission, on_delete=models.CASCADE, null=True,blank=True, db_column='idmission')
    class Meta:
        db_table = 'detailsc'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Budget(models.Model):
    nom=models.CharField(max_length=255,null=True)
    annee=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'budget'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Annee(models.Model):
    nom=models.CharField(max_length=255,null=True)
    choix=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    budget=models.CharField(max_length=255,null=True)
    defaut=models.CharField(max_length=255,null=True)
    fc=models.CharField(max_length=255,null=True)
    code = models.CharField(null=True,max_length=255)
    class Meta:
        db_table = 'annee'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Evaluationstructure(models.Model):
    score_periode_prec=models.CharField(max_length=255,null=True)
    score_periode_actuel_previ=models.CharField(max_length=255,null=True)
    score_periode_actuel_real=models.CharField(max_length=255,null=True)
    applicable=models.CharField(max_length=255,null=True)
    probleme=models.CharField(max_length=255,null=True)
    iddetailsc=models.ForeignKey(Detailsc, on_delete=models.CASCADE, null=True,blank=True, db_column='iddetailsc')
    idperiode=models.ForeignKey(Periode, on_delete=models.CASCADE, null=True,blank=True, db_column='idperiode')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True,blank=True, db_column='idbudget')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    class Meta:
        db_table = 'evaluationstructure'  # Specify the exact table name you want

    
class Sousrubrique(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    idrubrique=models.ForeignKey(Rubrique, on_delete=models.CASCADE, null=True,blank=True, db_column='idrubrique')
    class Meta:
        db_table = 'sousrubrique'  

    def __str__(self):
        return self.nom

class Rubriquemercurial(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'rubriquemercurial'  

    def __str__(self):
        return self.nom


class Sousrubriquemercurial(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    idrubriquemercurial=models.ForeignKey(Rubriquemercurial, on_delete=models.CASCADE, null=True,blank=True, db_column='idrubriquemercurial')
    class Meta:
        db_table = 'sousrubriquemercurial'  

    def __str__(self):
        return self.nom

class Groupe_utilisateur(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'groupe_utilisateur'  

    def __str__(self):
        return self.nom

class compteinstitution(models.Model):
    defaut=models.CharField(max_length=255,null=True)
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True,blank=True, db_column='idinstitution')
    idcompte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True,blank=True, db_column='idcompte')
    class Meta:
        db_table = 'compteinstitution'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Indicateurprogramme(models.Model):
    nom=models.CharField(max_length=255,null=True)
    objectif=models.CharField(max_length=255,null=True)
    periodicitecollecte=models.CharField(max_length=255,null=True)
    moyens=models.CharField(max_length=255,null=True)
    difficultes=models.CharField(max_length=255,null=True)
    pap=models.CharField(max_length=255,null=True)
    coefmulti=models.CharField(max_length=255,null=True)
    sourcedonnees=models.CharField(max_length=255,null=True)
    modecalcul=models.CharField(max_length=255,null=True)
    denominateur=models.CharField(max_length=255,null=True)
    numerateur=models.CharField(max_length=255,null=True)
    sourceverification=models.CharField(max_length=255,null=True)
    reference=models.CharField(max_length=255,null=True)
    annebaseline=models.CharField(max_length=255,null=True)
    annecible=models.CharField(max_length=255,null=True)
    unite=models.CharField(max_length=255,null=True)
    pourcentage=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    basline=models.CharField(max_length=255,null=True)
    valeurrealise=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    actif=models.CharField(max_length=255,null=True)
    periodicitemesure=models.CharField(max_length=255,null=True)
    commentaire=models.CharField(max_length=255,null=True)
    interpretation=models.CharField(max_length=255,null=True)
    limite=models.CharField(max_length=255,null=True)
    analyse=models.CharField(max_length=255,null=True)
    serviceanalyse=models.CharField(max_length=255,null=True)
    servicesynthese=models.CharField(max_length=255,null=True)
    servicevalidation=models.CharField(max_length=255,null=True)
    servicerespo=models.CharField(max_length=255,null=True)
    modecollecte=models.CharField(max_length=255,null=True)
    explication=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idprogramme')
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypedonnees')
    class Meta:
        db_table = 'indicateurprogramme'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Action(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    effet=models.CharField(max_length=255,null=True)
    cadremeo=models.CharField(max_length=255,null=True)
    respomeo=models.CharField(max_length=255,null=True)
    objectifs=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    indicateur=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    idzone=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, db_column='idzone')
    idindicateurprogramme=models.ForeignKey(Indicateurprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idindicateurprogramme')
    idprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idprogramme')
    class Meta:
        db_table = 'action'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Indicateuraction(models.Model):
    nom=models.CharField(max_length=255,null=True)
    objectif=models.CharField(max_length=255,null=True)
    periodicitecollecte=models.CharField(max_length=255,null=True)
    moyens=models.CharField(max_length=255,null=True)
    difficultes=models.CharField(max_length=255,null=True)
    pap=models.CharField(max_length=255,null=True)
    coefmulti=models.CharField(max_length=255,null=True)
    sourcedonnees=models.CharField(max_length=255,null=True)
    modecalcul=models.CharField(max_length=255,null=True)
    denominateur=models.CharField(max_length=255,null=True)
    numerateur=models.CharField(max_length=255,null=True)
    sourceverification=models.CharField(max_length=255,null=True)
    reference=models.CharField(max_length=255,null=True)
    annebaseline=models.CharField(max_length=255,null=True)
    annecible=models.CharField(max_length=255,null=True)
    unite=models.CharField(max_length=255,null=True)
    pourcentage=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    basline=models.CharField(max_length=255,null=True)
    valeurrealise=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    actif=models.CharField(max_length=255,null=True)
    periodicitemesure=models.CharField(max_length=255,null=True)
    commentaire=models.CharField(max_length=255,null=True)
    interpretation=models.CharField(max_length=255,null=True)
    limite=models.CharField(max_length=255,null=True)
    analyse=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    coutcollecte=models.CharField(max_length=255,null=True)
    serviceanalyse=models.CharField(max_length=255,null=True)
    servicesynthese=models.CharField(max_length=255,null=True)
    servicevalidation=models.CharField(max_length=255,null=True)
    servicerespo=models.CharField(max_length=255,null=True)
    modecollecte=models.CharField(max_length=255,null=True)
    explication=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypedonnees')
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True,blank=True, db_column='idaction')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    class Meta:
        db_table = 'indicateuraction'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Activite(models.Model):
    code = models.CharField(max_length=255,null=True)
    nom=models.CharField(max_length=255,null=True)
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    libelleobjectif=models.CharField(max_length=255,null=True)
    libelleindicateur=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'activite'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

    
class Tache(models.Model):
   nom=models.CharField(max_length=255,null=True)
   libelleobjectif=models.CharField(max_length=255,null=True)
   libelleindicateur=models.CharField(max_length=255,null=True)
   idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
   idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='activite')
   class Meta:
        db_table = 'tache'  # Specify the exact table name you want

   def __str__(self):
        return self.nom

class Cpte_grpusers(models.Model):
    idcompte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True,blank=True, db_column='idcompte')
    idgroupe_utilisateur=models.ForeignKey(Groupe_utilisateur, on_delete=models.CASCADE, null=True,blank=True, db_column='idgroupe_utilisateur')
    class Meta:
        db_table = 'cpte_grpusers'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Imputation(models.Model):
    code=models.CharField(max_length=255,null=True)
    nom=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idsousrubrique=models.ForeignKey(Sousrubrique, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousrubrique')
    idsection=models.ForeignKey(Section, on_delete=models.CASCADE, null=True,blank=True, db_column='idsection')
    idsousrubriquemercurial=models.ForeignKey(Sousrubriquemercurial, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousrubriquemercurial')
    idtypeimputation=models.ForeignKey(Typeimputation, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypeimputation')
    class Meta:
        db_table = 'imputation'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Moyens(models.Model):
    cp=models.CharField(max_length=255,null=True)
    ct=models.CharField(max_length=255,null=True)
    cu=models.CharField(max_length=255,null=True)
    qte=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    montantexecute=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregitre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    quantie=models.CharField(max_length=255,null=True)
    cpanneeplus1=models.CharField(max_length=255,null=True)
    cpanneeplus2=models.CharField(max_length=255,null=True)
    montant_paye=models.CharField(max_length=255,null=True)
    montant_ordonne=models.CharField(max_length=255,null=True)
    taxe_ordonne=models.CharField(max_length=255,null=True)
    nap_ordonne=models.CharField(max_length=255,null=True)
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True,blank=True, db_column='idbudget')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True,blank=True, db_column='idimputation')
    class Meta:
        db_table = 'moyens'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Indicateurprogrammeannee(models.Model):
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    valeurintermediaire=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    basline=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    unite=models.CharField(max_length=255,null=True)
    annebaseline=models.CharField(max_length=255,null=True)
    annecible=models.CharField(max_length=255,null=True)
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    idindicateurprogramme=models.ForeignKey(Indicateurprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idindicateurprogramme')
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypedonnees')
    class Meta:
        db_table = 'indicateurprogrammeannee'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Societe(models.Model):
    nom=models.CharField(max_length=255,null=True)
    ad1=models.CharField(max_length=255,null=True)
    contact=models.CharField(max_length=255,null=True)
    coge=models.CharField(max_length=255,null=True)
    auxi=models.CharField(max_length=255,null=True)
    ad2=models.CharField(max_length=255,null=True)
    ad3=models.CharField(max_length=255,null=True)
    pays=models.CharField(max_length=255,null=True)
    tel=models.CharField(max_length=255,null=True)
    fax=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=255,null=True)
    rib1=models.CharField(max_length=255,null=True)
    rib2=models.CharField(max_length=255,null=True)
    dom1=models.CharField(max_length=255,null=True)
    dom2=models.CharField(max_length=255,null=True)
    nbjours=models.CharField(max_length=255,null=True)
    jourref=models.CharField(max_length=255,null=True)
    cogeconsolide=models.CharField(max_length=255,null=True)
    auxiconsolide=models.CharField(max_length=255,null=True)
    datecre=models.DateTimeField(null=True,blank=True)
    datemaj=models.DateTimeField(null=True,blank=True)
    usecre=models.CharField(max_length=255,null=True)
    usermaj=models.CharField(max_length=255,null=True)
    planconsolide=models.CharField(max_length=255,null=True)
    statut=models.CharField(max_length=255,null=True)
    rc=models.CharField(max_length=255,null=True)
    nif=models.CharField(max_length=255,null=True)
    stat=models.CharField(max_length=255,null=True)
    bqnom=models.CharField(max_length=255,null=True)
    bqville=models.CharField(max_length=255,null=True)
    bqpays=models.CharField(max_length=255,null=True)
    bqswift=models.CharField(max_length=255,null=True)


    boite_postale= models.CharField(null=True,blank=True,max_length=255)
    localisation = models.CharField(max_length=255,null=True)
    registre = models.CharField(max_length=255,null=True)
    contribuable = models.CharField(max_length=255,null=True)
    cnps_number = models.CharField(max_length=255,null=True)


    class Meta:
        db_table = 'societe'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Signataire(models.Model):
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    nom=models.CharField(max_length=255,null=True)
    prenom=models.CharField(max_length=255,null=True)
    adresse=models.CharField(max_length=255,null=True)
    telephone=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'signataire'  

    def __str__(self):
        return self.nom
class Paragraphe(models.Model):
    code = models.CharField(max_length=255,null=True)
    nom=models.CharField(null=True,max_length=255)
    idsection = models.ForeignKey(Section,on_delete=models.CASCADE,null=True)
    idarticle = models.ForeignKey(Article,on_delete=models.CASCADE,null=True)

class Operation(models.Model):
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    nom=models.CharField(max_length=255,null=True)
    numordre=models.CharField(max_length=255,null=True)
    totalmontantaloue=models.CharField(max_length=255,null=True)
    moyensnecessaires=models.CharField(max_length=255,null=True)
    indicateurs2014=models.CharField(max_length=255,null=True)
    aeencours=models.CharField(max_length=255,null=True)
    cpconsommee=models.CharField(max_length=255,null=True)
    indicateurspoursuivis=models.CharField(max_length=255,null=True)
    valider=models.CharField(max_length=255,null=True)
    m1=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    m2=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    periodeexecution=models.CharField(max_length=255,null=True)
    montantengage=models.CharField(max_length=255,null=True)
    montantliquide=models.CharField(max_length=255,null=True)
    montantpayeht=models.CharField(max_length=255,null=True)
    montantpayettc=models.CharField(max_length=255,null=True)
    resultprocess=models.CharField(max_length=255,null=True)
    indicateurresult=models.CharField(max_length=255,null=True)
    montant_ordonne=models.CharField(max_length=255,null=True)
    taxe_ordonne=models.CharField(max_length=255,null=True)
    nap_ordonne=models.CharField(max_length=255,null=True)
    valeurattendue=models.CharField(max_length=255,null=True)
    justification=models.CharField(max_length=255,null=True)
    valeurrealisee=models.CharField(max_length=255,null=True)
    cpanneeplus1=models.CharField(max_length=255,null=True)
    cpanneeplus2=models.CharField(max_length=255,null=True)
    m3=models.CharField(max_length=255,null=True)
    m4=models.CharField(max_length=255,null=True)
    m5=models.CharField(max_length=255,null=True)
    m6=models.CharField(max_length=255,null=True)
    m7=models.CharField(max_length=255,null=True)
    m8=models.CharField(max_length=255,null=True)
    m9=models.CharField(max_length=255,null=True)
    m10=models.CharField(max_length=255,null=True)
    m11=models.CharField(max_length=255,null=True)
    m12=models.CharField(max_length=255,null=True)

    # idparagraphe = models.ManyToManyField(Paragraphe, related_name='operations')
    # idannee = models.ManyToManyField(Annee, related_name='operations')

    idsousprogramme= models.ForeignKey(Sousprogramme,on_delete=models.CASCADE,null=True)
    idsourcefinancement = models.ManyToManyField(Sourcefinacement,null=True)
    idtache=models.ForeignKey(Tache,on_delete=models.CASCADE,null=True)
    idevaluationstructure=models.ForeignKey(Evaluationstructure, on_delete=models.CASCADE, null=True,blank=True, db_column='idevaluationstructure')
    # periode_id=models.ForeignKey(Periode, on_delete=models.CASCADE, null=True,blank=True, db_column='periode_id')
    # idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    idnaturetache=models.ForeignKey(Naturetache, on_delete=models.CASCADE, null=True,blank=True, db_column='idnaturetache')
    # idnature_t=models.ForeignKey(Nature_t, on_delete=models.CASCADE, null=True,blank=True, db_column='idnature_t')
    idbailleurfond=models.ForeignKey(Bailleurfond, on_delete=models.CASCADE, null=True,blank=True, db_column='idbailleurfond')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idrisque=models.ForeignKey(Risque, on_delete=models.CASCADE, null=True,blank=True, db_column='idrisque')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
    idtypefinancement=models.ForeignKey(Typefinancement, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypefinancement')
    class Meta:
        db_table = 'operation'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
class Tva(models.Model):
    nom= models.CharField(null=True,max_length=255)

class OperationDetail(models.Model):
    idoperation = models.ForeignKey(Operation,on_delete=models.CASCADE,null=True)
    idannee=models.ForeignKey(Annee,on_delete=models.CASCADE,null=True)
    montant = models.IntegerField(null=True)
    idparagraphe=models.ForeignKey(Paragraphe,on_delete=models.CASCADE,null=True)
# class OperationDetailMontant(models.Model):
#     idoperation = models.ForeignKey(Operation,null=True,on_delete=models.CASCADE)
#     montant_global = models.IntegerField(null=True)
#     class Meta:
#         db_table = 'operationdetailmontant'  # Specify the exact table name you want


class Ir(models.Model):
    nom= models.CharField(null=True,max_length=255)
class Boncommande(models.Model):
    status= models.IntegerField(default=0)
    idtva=models.ForeignKey(Tva, on_delete=models.CASCADE, null=True,blank=True)
    idir=models.ForeignKey(Ir, on_delete=models.CASCADE, null=True,blank=True)
    idinstitution=models.ForeignKey(Institution,on_delete=models.CASCADE,null=True)
    idsociete=models.ForeignKey(Societe,on_delete=models.CASCADE,null=True)
    dateemission=models.DateTimeField(null=True,blank=True)
    object=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    delailivraison=models.CharField(max_length=255,null=True)
    totalht=models.CharField(max_length=255,null=True)
    tva=models.CharField(max_length=255,null=True)
    totalair=models.CharField(max_length=255,null=True)
    netapayer=models.CharField(max_length=255,null=True)
    avance=models.CharField(max_length=255,null=True)
    montantenlettre=models.CharField(max_length=50)
    ttc=models.CharField(max_length=255,null=True)
    espece=models.CharField(max_length=255,null=True)
    cheque=models.CharField(max_length=255,null=True)
    virement=models.CharField(max_length=255,null=True)
    datelivraison=models.CharField(max_length=255,null=True)
    engage=models.CharField(max_length=255,null=True)
    tauxtva=models.CharField(max_length=255,null=True)
    tauxair=models.CharField(max_length=255,null=True)
    reference=models.CharField(max_length=255,null=True)
    imputations=models.CharField(max_length=255,null=True)
    coefficientreducteur=models.CharField(max_length=255,null=True)
    verif=models.CharField(max_length=255,null=True)
    valide=models.CharField(max_length=255,null=True)
    nombreverif=models.CharField(max_length=255,null=True)
    bc=models.CharField(max_length=255,null=True)
    lettrecommande=models.CharField(max_length=255,null=True)
    mission=models.CharField(max_length=255,null=True)
    gre_a_gre=models.CharField(max_length=255,null=True)
    attentepayement=models.CharField(max_length=255,null=True)
    paye=models.CharField(max_length=255,null=True)
    liquide=models.CharField(max_length=255,null=True)
    montant_paye=models.CharField(max_length=255,null=True)
    salaire=models.CharField(max_length=255,null=True)
    montant_ordonne=models.CharField(max_length=255,null=True)
    taxe_ordonne=models.CharField(max_length=255,null=True)
    nap_ordonne=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'boncommande'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
class DetailBonCommande(models.Model):
    idboncommande = models.ForeignKey(Boncommande,on_delete=models.CASCADE,null=True)
    idparagraphe=models.ForeignKey(Paragraphe, on_delete=models.CASCADE, null=True,blank=True)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    # idsociete=models.ForeignKey(Societe, on_delete=models.CASCADE, null=True,blank=True, db_column='idsociete')
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True)
    idoperation=models.ForeignKey(Operation, on_delete=models.CASCADE, null=True,blank=True)
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True)

    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True)
    idparagraphe=models.ForeignKey(Paragraphe, on_delete=models.CASCADE, null=True,blank=True)
    

    class Meta:
        db_table ='detailboncommande'
    
class Criterestructure(models.Model):
    poids=models.CharField(max_length=255,null=True)
    point_max=models.CharField(max_length=255,null=True)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idcritere=models.ForeignKey(Critere, on_delete=models.CASCADE, null=True,blank=True, db_column='idcritere')
    class Meta:
        db_table = 'criterestructure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Structuremission(models.Model):
    problemes=models.CharField(max_length=255,null=True)
    objectif=models.CharField(max_length=255,null=True)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idmission=models.ForeignKey(Mission, on_delete=models.CASCADE, null=True,blank=True, db_column='idmission')
    class Meta:
        db_table = 'structuremission'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Tacheindicateurperformance(models.Model):
    cout=models.CharField(max_length=255,null=True)
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    class Meta:
        db_table = 'tacheindicateurperformance'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Typeperiode(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    defaut=models.CharField(max_length=255,null=True)
    idparent=models.ForeignKey(Parent, on_delete=models.CASCADE, null=True,blank=True, db_column='idparent')
    class Meta:
        db_table = 'typeperiode'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Action1(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    effet=models.CharField(max_length=255,null=True)
    cadremeo=models.CharField(max_length=255,null=True)
    respomeo=models.CharField(max_length=255,null=True)
    objectifs=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(max_length=255,null=True)
    indicateur=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    basline=models.CharField(max_length=255,null=True)
    idzone=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True,blank=True, db_column='idzone')
    idindicateurprogramme=models.ForeignKey(Indicateurprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idindicateurprogramme')
    idprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idprogramme')
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True,blank=True, db_column='idaction')
    class Meta:
        db_table = 'action1'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Structuremissionactivite(models.Model):
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
    objectif=models.CharField(max_length=255,null=True)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idmission=models.ForeignKey(Mission, on_delete=models.CASCADE, null=True,blank=True, db_column='idmission')
    class Meta:
        db_table = 'structuremissionactivite'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Tachebon(models.Model):
    nom=models.CharField(max_length=255,null=True)
    numordre=models.CharField(max_length=255,null=True)
    totalmonatntaloue=models.CharField(max_length=255,null=True)
    moyennecessaire=models.CharField(max_length=255,null=True)
    indicateur2014=models.CharField(max_length=255,null=True)
    aeencors=models.CharField(max_length=255,null=True)
    cpconsomee=models.CharField(max_length=255,null=True)
    indicateurpoursuivis=models.CharField(max_length=255,null=True)
    valider=models.CharField(max_length=255,null=True)
    m1=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    m2=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    m3=models.CharField(max_length=255,null=True)
    m4=models.CharField(max_length=255,null=True)
    m5=models.CharField(max_length=255,null=True)
    m6=models.CharField(max_length=255,null=True)
    m7=models.CharField(max_length=255,null=True)
    m8=models.CharField(max_length=255,null=True)
    m9=models.CharField(max_length=255,null=True)
    m10=models.CharField(max_length=255,null=True)
    m11=models.CharField(max_length=255,null=True)
    m12=models.CharField(max_length=255,null=True)
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
    idtypefinancement=models.ForeignKey(Typefinancement, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypefinancement')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idrisque=models.ForeignKey(Risque, on_delete=models.CASCADE, null=True,blank=True, db_column='idrisque')
    idbailleurfond=models.ForeignKey(Bailleurfond, on_delete=models.CASCADE, null=True,blank=True, db_column='idbailleurfond')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    idnature_t=models.ForeignKey(Nature_t, on_delete=models.CASCADE, null=True,blank=True, db_column='idnature_t')
    idnaturetache=models.ForeignKey(Naturetache, on_delete=models.CASCADE, null=True,blank=True, db_column='idnaturetache')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    class Meta:
        db_table = 'tachebon'  

    def __str__(self):
        return self.nom

class Utilisateurstructure(models.Model):
    idutilisateur=models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True,blank=True, db_column='idutilisateur')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    class Meta:
        db_table = 'utilisateurstructure'  

    def __str__(self):
        return self.nom

class  Verificationbc(models.Model):
    dateverification=models.DateTimeField(null=True,blank=True)
    observation=models.CharField(max_length=255,null=True)
    valide=models.CharField(max_length=255,null=True)
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True,blank=True, db_column='idboncommande')
    class Meta:
        db_table = 'verificationbc'  

    def __str__(self):
        return self.nom

class Activitestructure(models.Model):
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
    class Meta:
        db_table = 'activitestructure'  

    def __str__(self):
        return self.nom

class Activitetypestructure(models.Model):
     idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
     strategies=models.CharField(max_length=255,null=True)
     objectif=models.CharField(max_length=255,null=True)
     class Meta:
        db_table = 'activitetypestructure'  

     def __str__(self):
        return self.nom

class Personnel(models.Model):
    nom=models.CharField(max_length=255,null=True)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    class Meta:
        db_table = 'personnel'  

    def __str__(self):
        return self.nom

class Activitecorrectrices(models.Model):
    operation=models.CharField(max_length=255,null=True)
    montant=models.CharField(max_length=255,null=True)
    niveau=models.CharField(max_length=255,null=True)
    created_at=models.CharField(max_length=255,null=True)
    updated_at=models.CharField(max_length=255,null=True)
    statut=models.CharField(max_length=255,null=True)
    idperiode=models.ForeignKey(Periode, on_delete=models.CASCADE, null=True,blank=True, db_column='idperiode')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    idpersonnel=models.ForeignKey(Personnel, on_delete=models.CASCADE, null=True,blank=True, db_column='idpersonnel')
    class Meta:
        db_table = 'activitecorrectrices'  

    def __str__(self):
        return self.nom

class Methodeeval(models.Model):
    nom=models.CharField(max_length=255,null=True)
    description=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'methodeeval'  

    def __str__(self):
        return self.nom

class Origineindicateur(models.Model):
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'origineindicateur'  

    def __str__(self):
        return self.nom


class Indicateurperformance(models.Model):
    nom=models.CharField(max_length=255,null=True)
    periodicitecollecte=models.CharField(max_length=255,null=True)
    moyens=models.CharField(max_length=255,null=True)
    difficultes=models.CharField(max_length=255,null=True)
    pap=models.CharField(max_length=255,null=True)
    coefmulti=models.CharField(max_length=255,null=True)
    sourcedonnees=models.CharField(max_length=255,null=True)
    modecalcul=models.CharField(max_length=255,null=True)
    denominateur=models.CharField(max_length=255,null=True)
    numerateur=models.CharField(max_length=255,null=True)
    sourceverification=models.CharField(max_length=255,null=True)
    reference=models.CharField(max_length=255,null=True)
    annebaseline=models.CharField(max_length=255,null=True)
    annecible=models.CharField(max_length=255,null=True)
    unite=models.CharField(max_length=255,null=True)
    pourcentage=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    basline=models.CharField(max_length=255,null=True)
    valeurrealise=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    actif=models.CharField(max_length=255,null=True)
    periodicitemesure=models.CharField(max_length=255,null=True)
    commentaire=models.CharField(max_length=255,null=True)
    interpretation=models.CharField(max_length=255,null=True)
    limite=models.CharField(max_length=255,null=True)
    analyse=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    coutcollecte=models.CharField(max_length=255,null=True)
    serviceanalyse=models.CharField(max_length=255,null=True)
    servicesynthese=models.CharField(max_length=255,null=True)
    servicevalidation=models.CharField(max_length=255,null=True)
    servicerespo=models.CharField(max_length=255,null=True)
    modecollecte=models.CharField(max_length=255,null=True)
    explication=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypedonnees')
    idniveaupyramide=models.ForeignKey(Niveaupyramide, on_delete=models.CASCADE, null=True,blank=True, db_column='idaction')
    idorigineindicateur=models.ForeignKey(Origineindicateur, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    class Meta:
        db_table = 'indicateurperformance'  

    def __str__(self):
        return self.nom


class Extrant(models.Model):
    nom=models.CharField(max_length=255,null=True)
    cout=models.CharField(max_length=255,null=True)
    indicateurs=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idmethodeeval=models.ForeignKey(Methodeeval, on_delete=models.CASCADE, null=True,blank=True, db_column='idmethodeeval')
    idindicateurperformance=models.ForeignKey(Indicateurperformance, on_delete=models.CASCADE, null=True,blank=True, db_column='idindicateurperformance')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
    class Meta:
        db_table = 'extrant'  

    def __str__(self):
        return self.nom


class Importextrant(models.Model):
    nom=models.CharField(max_length=255,null=True)
    idextrant=models.ForeignKey(Extrant, on_delete=models.CASCADE, null=True,blank=True, db_column='idextrant')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
    class Meta:
        db_table = 'importextrant'  

    def __str__(self):
        return self.nom
    
class Elementcout(models.Model):
    nom=models.CharField(max_length=255,null=True)
    prixunitaire=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    conditionnement = models.CharField(null=True,max_length=255)
    # idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True,blank=True, db_column='idimputation')
    idrubriquemercurial=models.ForeignKey(Rubrique, on_delete=models.CASCADE, null=True,blank=True, db_column='idrubriquemercuriale')
    # idunite=models.ForeignKey(Unite, on_delete=models.CASCADE, null=True,blank=True, db_column='idunite')
    idsousrubriquemercurial=models.ForeignKey(Sousrubrique, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousrubriquemercurial')
    class Meta:
        db_table = 'elementcout'  

    def __str__(self):
        return self.nom

class Exercice(models.Model):
    coutglobal=models.CharField(max_length=255,null=True)
    nom_exercice=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    montantaccorde=models.CharField(max_length=255,null=True)
    ispublicpropbudgetsante=models.CharField(max_length=255,null=True)
    montantreel=models.CharField(max_length=255,null=True)
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True,blank=True, db_column='idinstitution')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    class Meta:
        db_table = 'exercice'  

    def __str__(self):
        return self.nom

class Exercise_action(models.Model):
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True,blank=True, db_column='idaction')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True,blank=True, db_column='idexercice')
    tauxacceptable=models.CharField(max_length=255,null=True)
    coutprogaction=models.CharField(max_length=255,null=True)
    poidaction=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    etat=models.CharField(max_length=255,null=True)
    # derniere_modif=models.CharField(null=True,blank=True)
    class Meta:
        db_table = 'exercice_action'  

    def __str__(self):
        return self.nom

class Exercice_nature(models.Model):
    montant=models.CharField(max_length=255,null=True)
    pourcentage=models.CharField(max_length=255,null=True)
    idnature_t=models.ForeignKey(Nature_t, on_delete=models.CASCADE, null=True,blank=True, db_column='idnature_t')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True,blank=True, db_column='idexercice')
    class Meta:
        db_table = 'exercice_nature'  

    def __str__(self):
        return self.nom


class Exercicenature_t(models.Model):
    montant=models.CharField(max_length=255,null=True)
    pourcentage=models.CharField(max_length=255,null=True)
    idnature_t=models.ForeignKey(Nature_t, on_delete=models.CASCADE, null=True,blank=True, db_column='idnature_t')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True,blank=True, db_column='idexercice')
    class Meta:
        db_table = 'exercicenature_t'  

    def __str__(self):
        return self.nom

class Exercicetypefinancement(models.Model):
    montant=models.CharField(max_length=255,null=True)
    pourcentage=models.CharField(max_length=255,null=True)
    idtypefinancement=models.ForeignKey(Typefinancement, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypefinancement')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True,blank=True, db_column='idexercice')
    class Meta:
        db_table = 'exercicetypefinancement'  

    def __str__(self):
        return self.nom

class Exercise_programme(models.Model):
    nom=models.CharField(max_length=255,null=True)
    coutprog=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True,blank=True, db_column='idexercice')
    class Meta:
        db_table = 'exercice_programme'  

    def __str__(self):
        return self.nom
class Ordre_payement(models.Model):
     beneficiaire=models.CharField(max_length=255,null=True)
     montant=models.CharField(max_length=255,null=True)
     taxe=models.CharField(max_length=255,null=True)
     nap=models.CharField(max_length=255,null=True)
     montant_en_lettre=models.CharField(max_length=255,null=True)
     detail_nap=models.CharField(max_length=255,null=True)
     detail_tva=models.CharField(max_length=255,null=True)
     detail_air=models.CharField(max_length=255,null=True)
     pieces=models.CharField(max_length=255,null=True)
     etat=models.CharField(max_length=255,null=True)
     code=models.CharField(max_length=255,null=True)
     objet=models.CharField(max_length=255,null=True)
     mode_paiement=models.CharField(max_length=255,null=True)
     nombre_verification=models.CharField(max_length=255,null=True)
     pays=models.CharField(max_length=255,null=True) 
     date_ordonnation=models.DateTimeField(null=True,blank=True)
     idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True,blank=True, db_column='idboncommande')
     class Meta:
        db_table = 'ordre_payement'  

     def __str__(self):
        return self.nom

class Verifiaction_op(models.Model):
    # date_verification=models.CharField(null=True,blank=True)
    valide=models.CharField(max_length=255,null=True)
    idordre_payement=models.ForeignKey(Ordre_payement, on_delete=models.CASCADE, null=True,blank=True, db_column='idordre_payement')
    class Meta:
        db_table = 'verification_op'  

    def __str__(self):
        return self.nom

class Ligne_decision(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    coutunitaire=models.CharField(max_length=255,null=True)
    quantite=models.CharField(max_length=255,null=True)
    total=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    verif=models.CharField(max_length=255,null=True)
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True,blank=True, db_column='idboncommande')
    class Meta:
        db_table = 'ligne_decision'  

    def __str__(self):
        return self.nom

class Ligneboncommande(models.Model):
    prixunitaire=models.CharField(max_length=255,null=True)
    quantite=models.CharField(max_length=255,null=True)
    total=models.IntegerField(null=True)
    prixmercurial=models.CharField(max_length=255,null=True)
    verif=models.CharField(max_length=255,null=True)
    references=models.CharField(max_length=255,null=True)
    idelementcout=models.ForeignKey(Elementcout, on_delete=models.CASCADE, null=True,blank=True, db_column='idelementcout')
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True,blank=True, db_column='idboncommande')
    class Meta:
        db_table = 'ligneboncommande'  

    def __str__(self):
        return self.nom

class Ligne_verification_bc(models.Model):
    idverificationbc=models.ForeignKey(Verificationbc, on_delete=models.CASCADE, null=True,blank=True, db_column='idverificationbc')
    idligne_decision=models.ForeignKey(Ligne_decision, on_delete=models.CASCADE, null=True,blank=True, db_column='idligne_decision')
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True,blank=True, db_column='idboncommande')
    class Meta:
        db_table = 'ligne_verification_bc'  

    def __str__(self):
        return self.nom

class Menu(models.Model):
    name=models.CharField(max_length=255,null=True)
    libelle=models.CharField(max_length=255,null=True)
    shortcut=models.CharField(max_length=255,null=True)
    categorie=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    # date_enregistre=models.CharField(null=True,blank=True)
    # derniere_modif=models.CharField(null=True,blank=True)
    id_parent=models.ForeignKey(Parent, on_delete=models.CASCADE, null=True,blank=True, db_column='id_parent')
    class Meta:
        db_table = 'menu'  

    def __str__(self):
        return self.nom

class Recette(models.Model):
    ranneeavant=models.CharField(max_length=255,null=True)
    reaaneeavant=models.CharField(max_length=255,null=True)
    prannee_plus_1_cout=models.CharField(max_length=255,null=True)
    prannee_plus_1_qte=models.CharField(max_length=255,null=True)
    prannee_plus_1_total=models.CharField(max_length=255,null=True)
    prannee_plus_2_cout=models.CharField(max_length=255,null=True)
    qte=models.CharField(max_length=255,null=True)
    cu=models.CharField(max_length=255,null=True)
    ct=models.CharField(max_length=255,null=True)
    prannee_plus_2_qte=models.CharField(max_length=255,null=True)
    prannee_plus_2_total=models.CharField(max_length=255,null=True)
    ranneeavant_qte=models.CharField(max_length=255,null=True)
    ranneeavant_cu=models.CharField(max_length=255,null=True)
    raneeavant_qte=models.CharField(max_length=255,null=True)
    montant_consomme_avant=models.CharField(max_length=255,null=True)
    reaanneeavant_cu=models.CharField(max_length=255,null=True)
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    idbailleurfond=models.ForeignKey(Bailleurfond, on_delete=models.CASCADE, null=True,blank=True, db_column='idbailleurfond')
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True,blank=True, db_column='idimputation')
    class Meta:
        db_table = 'recette'  

    def __str__(self):
        return self.nom

class Indicateuractivite(models.Model):
    nom=models.CharField(max_length=255,null=True)
    periodicitecollecte=models.CharField(max_length=255,null=True)
    moyens=models.CharField(max_length=255,null=True)
    difficultes=models.CharField(max_length=255,null=True)
    pap=models.CharField(max_length=255,null=True)
    coefmulti=models.CharField(max_length=255,null=True)
    sourcedonnees=models.CharField(max_length=255,null=True)
    modecalcul=models.CharField(max_length=255,null=True)
    denominateur=models.CharField(max_length=50)
    numerateur=models.CharField(max_length=50)
    sourceverification=models.CharField(max_length=50)
    reference=models.CharField(max_length=255,null=True)
    annebaseline=models.CharField(max_length=255,null=True)
    annecible=models.CharField(max_length=255,null=True)
    unite=models.CharField(max_length=255,null=True)
    pourcentage=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    basline=models.CharField(max_length=255,null=True)
    valeurrealise=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    actif=models.CharField(max_length=255,null=True)
    periodicitemesure=models.CharField(max_length=255,null=True)
    commentaire=models.CharField(max_length=255,null=True)
    interpretation=models.CharField(max_length=255,null=True)
    limite=models.CharField(max_length=255,null=True)
    analyse=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    coutcollecte=models.CharField(max_length=255,null=True)
    serviceanalyse=models.CharField(max_length=255,null=True)
    servicesynthese=models.CharField(max_length=255,null=True)
    servicevalidation=models.CharField(max_length=255,null=True)
    servicerespo=models.CharField(max_length=255,null=True)
    modecollecte=models.CharField(max_length=255,null=True)
    explication=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    hypothese_risque=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    idactvite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypedonnees')
    class Meta:
        db_table = 'indicateuractivite'  

    def __str__(self):
        return self.nom

class Mois(models.Model):
    nom=models.CharField(max_length=255,null=True)
    rang=models.CharField(max_length=255,null=True)
    choix=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'mois'  

    def __str__(self):
        return self.nom

class Semaine(models.Model):
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    idmois=models.ForeignKey(Mois, on_delete=models.CASCADE, null=True,blank=True, db_column='idmois')
    s4=models.CharField(max_length=255,null=True)
    s3=models.CharField(max_length=255,null=True)
    s2=models.CharField(max_length=255,null=True)
    s1=models.CharField(max_length=255,null=True)
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'semaine'  

    def __str__(self):
        return self.nom

class Moyens1(models.Model):
    cp=models.CharField(max_length=255,null=True)
    ct=models.CharField(max_length=255,null=True)
    cu=models.CharField(max_length=255,null=True)
    qte=models.CharField(max_length=255,null=True)
    montantexecute=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    quantite=models.CharField(max_length=255,null=True)
    cpanneeplus1=models.CharField(max_length=255,null=True)
    cpanneeplus2=models.CharField(max_length=255,null=True)
    idmoyens=models.ForeignKey(Moyens, on_delete=models.CASCADE, null=True,blank=True, db_column='idmoyens')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True,blank=True, db_column='idbudget')
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True,blank=True, db_column='idimputation')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'moyens1'  

    def __str__(self):
        return self.nom

class Moyensbon(models.Model):
    cp=models.CharField(max_length=255,null=True)
    ct=models.CharField(max_length=255,null=True)
    cu=models.CharField(max_length=255,null=True)
    qte=models.CharField(max_length=255,null=True)
    montantexecute=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    quantite=models.CharField(max_length=255,null=True)
    cpanneeplus1=models.CharField(max_length=255,null=True)
    cpanneeplus2=models.CharField(max_length=255,null=True)
    idmoyens=models.ForeignKey(Moyens, on_delete=models.CASCADE, null=True,blank=True, db_column='idmoyens')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True,blank=True, db_column='idbudget')
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True,blank=True, db_column='idimputation')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'moyensbon'  

    def __str__(self):
        return self.nom
    
class Cdmt(models.Model):
    nom=models.CharField(max_length=255,null=True)
    anneedebut=models.DateField(max_length=255,null=True)
    anneefin=models.DateField(max_length=255,null=True)
    class Meta:
        db_table = 'cdmt'  

    def __str__(self):
        return self.nom

class Budget_tache(models.Model):
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True,blank=True, db_column='idbudget')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    idbailleurfond=models.ForeignKey(Bailleurfond, on_delete=models.CASCADE, null=True,blank=True, db_column='idbailleurfond')
    idrisque=models.ForeignKey(Risque, on_delete=models.CASCADE, null=True,blank=True, db_column='idrisque')
    class Meta:
        db_table = 'budget_tache'  

    def __str__(self):
        return self.nom


class Parametre(models.Model):
     idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True,blank=True, db_column='idcdmt')
     class Meta:
        db_table = 'parametre'  

     def __str__(self):
        return self.nom

class Parametrage(models.Model):
    tauxtva=models.CharField(max_length=255,null=True)
    tauxair=models.CharField(max_length=255,null=True)
    repertoire_photo=models.CharField(max_length=255,null=True)
    pourcentagemercurial=models.CharField(max_length=255,null=True)
    user_tompro=models.CharField(max_length=255,null=True)
    password_tompro=models.CharField(max_length=255,null=True)
    user_gendata=models.CharField(max_length=255,null=True)
    password_gendata=models.CharField(max_length=255,null=True)
    chaine_connexion_gendata=models.CharField(max_length=255,null=True)
    driver_class_name_gendata=models.CharField(max_length=255,null=True)
    data_base_name_tompro=models.CharField(max_length=255,null=True)
    driver_class_name_tompro=models.CharField(max_length=255,null=True)
    database_name_gendata=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'parametrage'  

    def __str__(self):
        return self.nom
    
class Cdmt_annee(models.Model):
    idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True,blank=True, db_column='idcdmt')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    rang=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'cdmt_annee'  

    def __str__(self):
        return self.nom

class Cdmt_tache(models.Model):
    ri1=models.CharField(max_length=255,null=True)
    ri2=models.CharField(max_length=255,null=True)
    ri3=models.CharField(max_length=255,null=True)
    re1=models.CharField(max_length=255,null=True)
    re2=models.CharField(max_length=255,null=True)
    re3=models.CharField(max_length=255,null=True)
    aeannee1=models.CharField(max_length=255,null=True)
    idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True,blank=True, db_column='idcdmt')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    class Meta:
        db_table = 'cdmt_tache'  

    def __str__(self):
        return self.nom
    
class Cdmt_tachebon(models.Model):
    ri1=models.CharField(max_length=255,null=True)
    ri2=models.CharField(max_length=255,null=True)
    ri3=models.CharField(max_length=255,null=True)
    re1=models.CharField(max_length=255,null=True)
    re2=models.CharField(max_length=255,null=True)
    re3=models.CharField(max_length=255,null=True)
    aeannee1=models.CharField(max_length=255,null=True)
    idcdmt_tache=models.ForeignKey(Cdmt_tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idcdmt_tache')
    idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True,blank=True, db_column='idcdmt')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    class Meta:
        db_table = 'cdmt_tachebon'  

    def __str__(self):
        return self.nom
    
class Cdmt_tacheok(models.Model):
    ri1=models.CharField(max_length=255,null=True)
    ri2=models.CharField(max_length=255,null=True)
    ri3=models.CharField(max_length=255,null=True)
    re1=models.CharField(max_length=255,null=True)
    re2=models.CharField(max_length=255,null=True)
    re3=models.CharField(max_length=255,null=True)
    aeannee1=models.CharField(max_length=255,null=True)
    idcdmt_tache=models.ForeignKey(Cdmt_tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idcdmt_tache')
    idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True,blank=True, db_column='idcdmt')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    class Meta:
        db_table = 'cdmt_tacheok'  

    def __str__(self):
        return self.nom


class Certificatengagement(models.Model):
    idmoyens=models.ForeignKey(Moyens, on_delete=models.CASCADE, null=True,blank=True, db_column='idmoyens')
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True,blank=True, db_column='idboncommande')
    dateengagement=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'certificatengagement'  

    def __str__(self):
        return self.nom
    

class Chronogrammes(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    created_at=models.CharField(max_length=255,null=True)
    updated_at=models.CharField(max_length=255,null=True)
    idperiode=models.ForeignKey(Periode,  on_delete=models.CASCADE, null=True,blank=True, db_column='idperiode')
    Activitecorrectrices_id=models.ForeignKey(Activitecorrectrices,  on_delete=models.CASCADE, null=True,blank=True, db_column='activitecorrectrice_id')
    idperiodeparent=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'chronogrammes'  

    def __str__(self):
        return self.nom
    
class Virement(models.Model):
    nom = models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'virement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Payement(models.Model):
    ribbeneficiaire=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    reference=models.CharField(max_length=255,null=True)
    objet=models.CharField(max_length=255,null=True)
    montant=models.CharField(max_length=255,null=True)
    bc=models.CharField(max_length=255,null=True)
    lc=models.CharField(max_length=255,null=True)
    decision=models.CharField(max_length=255,null=True)
    mission=models.CharField(max_length=255,null=True)
    salaire=models.CharField(max_length=255,null=True)
    facture=models.CharField(max_length=255,null=True)
    datesaisie=models.DateTimeField(max_length=255,null=True)
    datevalidation=models.DateTimeField(max_length=255,null=True)
    database_name_gendata=models.CharField(max_length=255,null=True)
    virement_id=models.ForeignKey(Virement, on_delete=models.CASCADE, null=True,blank=True, db_column='virement_id')
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True,blank=True, db_column='idboncommande')
    idordre_payement=models.ForeignKey(Ordre_payement, on_delete=models.CASCADE, null=True,blank=True, db_column='idordre_payement')
    class Meta:
        db_table = 'payement'  

    def __str__(self):
        return self.nom

class Periodes(models.Model):
    libelle=models.CharField(max_length=255,null=True)
    rang=models.CharField(max_length=255,null=True)
    idtypeperiode=models.ForeignKey(Typeperiode, on_delete=models.CASCADE, null=True,blank=True, db_column='idtypeperiode')
    class Meta:
        db_table = 'periodes'  

    def __str__(self):
        return self.nom

class Periodetaches(models.Model):
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True,blank=True, db_column='idtache')
    idperiode=models.ForeignKey(Periode, on_delete=models.CASCADE, null=True,blank=True, db_column='idperiode')
    valeurrealisee=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'periodetaches'  

    def __str__(self):
        return self.nom

class Performance(models.Model):
    justification=models.CharField(max_length=255,null=True)
    annepta=models.CharField(max_length=255,null=True)
    sourceverification=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    baseline=models.CharField(max_length=255,null=True)
    conditionreussite=models.CharField(max_length=255,null=True)
    sourecverifiactionanterieur=models.CharField(max_length=255,null=True)
    cibleanterieur=models.CharField(max_length=255,null=True)
    reductionecart=models.CharField(max_length=255,null=True)
    ecart=models.CharField(max_length=255,null=True)
    objectifspecifique=models.CharField(max_length=255,null=True)
    confditionreussite=models.CharField(max_length=100)
    enonceprojet=models.CharField(max_length=255,null=True)
    actioncorrectrices=models.CharField(max_length=255,null=True)
    conclusion=models.CharField(max_length=255,null=True)
    recommandation=models.CharField(max_length=255,null=True)
    criteresvalidation=models.CharField(max_length=255,null=True)
    valeurealise=models.CharField(max_length=50)
    observations=models.CharField(max_length=255,null=True)
    baselineanterieur=models.CharField(max_length=255,null=True)
    idindicateurperformance=models.ForeignKey(Indicateurperformance, on_delete=models.CASCADE, null=True,blank=True, db_column='idindicateurperformance')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True,blank=True, db_column='idstructure')
    idmission=models.ForeignKey(Mission, on_delete=models.CASCADE, null=True,blank=True, db_column='idmission')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True,blank=True, db_column='idactivite')
    class Meta:
        db_table = 'performance'  

    def __str__(self):
        return self.nom

class Rubriquedifficulte(models.Model):
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    nom=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'rubriquedifficulte'  

    def __str__(self):
        return self.nom

class Revue(models.Model):
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True,blank=True, db_column='idannee')
    # nom=models.CharField(null=True,blank=True)
    # etat=models.CharField(null=True,blank=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'revue'  

    def __str__(self):
        return self.nom

class Revueactivite(models.Model):
    activites=models.CharField(max_length=255,null=True)
    cout=models.CharField(max_length=255,null=True)
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True,blank=True, db_column='idrevue')
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    observations=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'revueactivite'  

    def __str__(self):
        return self.nom

class Revuefait(models.Model):
    fait=models.CharField(max_length=255,null=True)
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True,blank=True, db_column='idrevue')
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    observations=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    implications=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'revuefait'  

    def __str__(self):
        return self.nom

class Revueprogramme(models.Model):
    fait=models.CharField(max_length=255,null=True)
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True,blank=True, db_column='idrevue')
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    observations=models.CharField(max_length=255,null=True)
    cout=models.CharField(max_length=255,null=True)
    produits=models.CharField(max_length=255,null=True)
    contextmeo=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    difficultes=models.CharField(max_length=255,null=True)
    prisencompte=models.CharField(max_length=255,null=True)
    ajustementactions=models.CharField(max_length=255,null=True)
    implications=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'revueprogramme'  

    def __str__(self):
        return self.nom

class Revueperformance(models.Model):
    tauxrealise=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    indicateur=models.CharField(max_length=255,null=True)
    valeurcible=models.CharField(max_length=255,null=True)
    valeurrealise=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    # derniere_modif=models.CharField(null=True,blank=True)
    # date_enregistre=models.CharField(null=True,blank=True)
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True,blank=True, db_column='idrevue')
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    class Meta:
        db_table = 'revueperformance'  

    def __str__(self):
        return self.nom

class Revuedifficilte(models.Model):
    difficulte=models.CharField(max_length=255,null=True)
    solution=models.CharField(max_length=255,null=True)
    observations=models.CharField(max_length=255,null=True)
    idrubriquedifficulte=models.ForeignKey(Rubriquedifficulte, on_delete=models.CASCADE, null=True,blank=True, db_column='idrubriquedifficulte')
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True,blank=True, db_column='idrevue')
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    etat=models.CharField(max_length=255,null=True)
    # derniere_modif=models.CharField(null=True,blank=True)
    # date_enregistre=models.CharField(null=True,blank=True)
    class Meta:
        db_table = 'revuedifficilte'  

    def __str__(self):
        return self.nom



class Revueaction(models.Model):
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True,blank=True, db_column='idaction')
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True,blank=True, db_column='idrevue')
    activitesupprimes=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'revueaction'  

    def __str__(self):
        return self.nom

class Indicateurextrant(models.Model):
    idindicateuractivite=models.ForeignKey(Indicateuractivite, on_delete=models.CASCADE, null=True,blank=True, db_column='idindicateuractivite')
    idextrant=models.ForeignKey(Extrant, on_delete=models.CASCADE, null=True,blank=True, db_column='idextrant')
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True,blank=True, db_column='idaction')
    cible=models.CharField(max_length=255,null=True)
    observation=models.CharField(max_length=255,null=True)
    class Meta:
        db_table = 'indicateurextrant'  

    def __str__(self):
        return self.nom

class Privilege(models.Model):
    idcompte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True,blank=True, db_column='idcompte')
    idgroupe_utilisateur=models.ForeignKey(Groupe_utilisateur, on_delete=models.CASCADE, null=True,blank=True, db_column='idgroupe_utilisateur')
    configuration=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    class Meta:
        db_table = 'privilege'  

    def __str__(self):
        return self.nom

class Privilege_b(models.Model):
     idmenu=models.ForeignKey(Menu, on_delete=models.CASCADE, null=True,blank=True, db_column='idmenu')
     idcompte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True,blank=True, db_column='idcompte')
     class Meta:
        db_table = 'privilege_b'  

     def __str__(self):
        return self.nom


class Sousrogramme1(models.Model):
    nom=models.CharField(max_length=255,null=True)
    code=models.CharField(max_length=255,null=True)
    stratrgieprogramme=models.CharField(max_length=255,null=True)
    respomeo=models.CharField(max_length=255,null=True)
    cadremeo=models.CharField(max_length=255,null=True)
    impact=models.CharField(max_length=255,null=True)
    etat=models.CharField(max_length=255,null=True)
    derniere_modif=models.DateTimeField(null=True,blank=True)
    objectifs=models.CharField(max_length=255,null=True)
    objectifstrategique=models.CharField(max_length=255,null=True)
    fonction=models.CharField(max_length=255,null=True)
    indicateur=models.CharField(max_length=255,null=True)
    baseline=models.CharField(max_length=255,null=True)
    cible=models.CharField(max_length=255,null=True)
    date_enregistre=models.DateTimeField(null=True,blank=True)
    idsousprogramme=models.ForeignKey(Sousprogramme, on_delete=models.CASCADE, null=True,blank=True, db_column='idsousprogramme')
    idsoussecteur=models.ForeignKey(Soussecteur, on_delete=models.CASCADE, null=True,blank=True, db_column='idsoussecteur')
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True,blank=True, db_column='idinstitution')
    idaxestrategique=models.ForeignKey(Axestrategique, on_delete=models.CASCADE, null=True,blank=True, db_column='idaxestrategique')
    class Meta:
        db_table = 'programme1'  

    def __str__(self):
        return self.nom

class Decision(models.Model):
    numero = models.CharField(null=True,max_length=255)
    date = models.DateField(null=True)
    objet= models.CharField(max_length=255,null=True)
    montant=models.CharField(null=True)
    iduser = models.ForeignKey(Utilisateur,on_delete=models.CASCADE,null=True)
























   



























    

    





   
    






    
    





    






    



    






    





                    
                                   
    








    




















