from django.db import models
from django.utils.timezone import datetime



class Statutmatrimonial(models.Model):
    idstatutmatrimonial=models.AutoField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'statutmatrimonial'  

    def __str__(self):
        return self.nom
    
class Risque(models.Model):
    idrisque=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'risque'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Naturetache(models.Model):
    idnaturetache=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    class Meta:
        db_table = 'naturetache'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Sourcefinacement(models.Model):
    idsourcefinancement=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'sourcefinancement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom


class Frequence(models.Model):
    idfrequence=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    class Meta:
        db_table = 'frequence'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Basejuridique(models.Model):
    idbasejuridique=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'basejuridique'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Axestrategique(models.Model):
    idaxestrategique=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'axestrategique'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
   
class Rang(models.Model):
    idrang=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=50)
    numero=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'rang'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
   

class Typedonnees(models.Model):
    idtypedonnees=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'typedonnees'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
   

class Zone(models.Model):
    idzone=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'zone'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Typeactivite(models.Model):
    idtypeactivite=models.AutoField(primary_key=True,null=False)
    nom=models.CharField(max_length=50)
    numero=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'typeactivite'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Niveaupyramide(models.Model):
    idcode=models.CharField(primary_key=True, null=False)
    code=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'niveaupyramide'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Rattachement(models.Model):
    idrattachement=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    class Meta:
        db_table = 'rattachement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
   
class Statstructure(models.Model):
    idstatutstructure=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'statstructure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Typestructure(models.Model):
    idtypestructure = models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'typestructure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Article(models.Model):
    idarticle=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    class Meta:
        db_table = 'article'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Typeimputation(models.Model):
    idtypeimputation=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    class Meta:
        db_table = 'typeimputation'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Composante(models.Model):
    idcomposante=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    class Meta:
        db_table = 'composante'  # Specify the exact table name you want

    def __str__(self):
        return self.nom


class Critere(models.Model):
    idcritere=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    poids=models.CharField(max_length=50)
    class Meta:
        db_table = 'critere'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Unite(models.Model):
    idunite=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    class Meta:
        db_table = 'unite'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Menu_b(models.Model):
    idmenu_b=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    ressource=models.CharField(max_length=50)
    class Meta:
        db_table = 'menu_b'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Rubrique(models.Model):
    idrubrique=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    class Meta:
        db_table = 'rubrique'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Reglage(models.Model):
    idreglage=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    valeur=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'reglage'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Parametres(models.Model):
    idparametres=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    valeur=models.CharField(max_length=50)
    min=models.CharField(max_length=50)
    max=models.CharField(max_length=50)
    class Meta:
        db_table = 'parametres'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Secteur(models.Model):
    idsecteur=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'secteur'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

   
class Pap(models.Model):
    idpap=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'pap'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Parent(models.Model):
    idparent=models.AutoField(primary_key=True, null=False)
    
    nom = models.CharField(max_length=50)
    class Meta:
        db_table = 'parent'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

    
class Continent(models.Model):
    idcontinent=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'continent'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Pays(models.Model):
    idpays=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    drapeau=models.CharField(max_length=50)
    drapeau_relatif=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    id_continent=models.ForeignKey(Continent, on_delete=models.CASCADE, null=True, db_column='id_continent')
    class Meta:
        db_table = 'pays'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Region(models.Model):
    idregion=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    superfiecie=models.CharField(max_length=50)
    population=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    id_pays=models.ForeignKey(Pays, on_delete=models.CASCADE, null=True, db_column='id_pays')
    class Meta:
        db_table = 'region'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Departement(models.Model):
    iddepartement=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idregion=models.ForeignKey(Region, on_delete=models.CASCADE, null=True, db_column='idregion')
    class Meta:
        db_table = 'departement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Arrondissement(models.Model):
    idarrondissement=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    id_departement=models.ForeignKey(Departement, on_delete=models.CASCADE, null=True, db_column='id_departement')
    class Meta:
        db_table = 'arrondissement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Ville(models.Model):
    idville=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    id_pays=models.ForeignKey(Pays, on_delete=models.CASCADE, null=True, db_column='id_pays')
    class Meta:
        db_table = 'ville'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Quartier(models.Model):
    idquartier=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    id_ville=models.ForeignKey(Ville, on_delete=models.CASCADE, null=True, db_column='id_ville')
    class Meta:
        db_table = 'quartier'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Rue(models.Model):
    idrue=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistrement=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    id_quartier=models.ForeignKey(Quartier, on_delete=models.CASCADE, null=True, db_column='id_quartier')
    class Meta:
        db_table = 'rue'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Adresse(models.Model):
    idaddresse=models.CharField(primary_key=True, null=False)
    contact=models.CharField(max_length=50)
    fax=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    bp=models.CharField(max_length=50)
    siteweb=models.CharField(max_length=50)
    id_quartier=models.ForeignKey(Quartier, on_delete=models.CASCADE, null=True, db_column='id_quartier')
    id_rue=models.ForeignKey(Rue, on_delete=models.CASCADE, null=True, db_column='id_rue')
    id_ville=models.ForeignKey(Ville, on_delete=models.CASCADE, null=True, db_column='id_ville')
    class Meta:
        db_table = 'adresse'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    idutilisateur=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=70)
    prenom=models.CharField(max_length=70)
    date_enregistre=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    date_naissance=models.CharField(max_length=50)
    cni=models.CharField(max_length=50)
    id_arrondissement=models.ForeignKey(Arrondissement, on_delete=models.CASCADE, null=True, db_column='id_arrondissement')
    id_statut_matrimonial=models.ForeignKey(Statutmatrimonial, on_delete=models.CASCADE, null=True, db_column='id_statut_matrimonial')
    id_pays=models.ForeignKey(Pays, on_delete=models.CASCADE, null=True, db_column='id_pays')
    id_adresse=models.ForeignKey(Adresse, on_delete=models.CASCADE, null=True, db_column='id_adresse')
    class Meta:
        db_table = 'utilisateur'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Compte(models.Model):
    idcompte=models.CharField(primary_key=True, null=False)
    login=models.CharField(max_length=50)
    mdp=models.CharField(max_length=50)
    langue=models.CharField(max_length=50)
    connexion=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    heure_denregistre=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    id_utilisateur=models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, db_column='id_utilisateur')
    class Meta:
        db_table = 'compte'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Operation(models.Model):
    idoperation=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    adresseip=models.CharField(max_length=50)
    adressemac=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    adressenom=models.CharField(max_length=50)
    heure_operation=models.CharField(max_length=50)
    date_operation=models.CharField(max_length=50)
    id_compte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True, db_column='id_compte')
    class Meta:
        db_table = 'operation'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Nature_t(models.Model):
    idnature_t=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=60)
    idnaturetache=models.ForeignKey(Naturetache, on_delete=models.CASCADE, null=True, db_column='idnaturetache')
    class Meta:
        db_table = 'nature_t'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Bailleurfond(models.Model):
    idbailleurfond=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=70)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idsourcefinancement=models.ForeignKey(Sourcefinacement, on_delete=models.CASCADE, null=True, db_column='idsourcefinancement')
    class Meta:
        db_table = 'bailleurfond'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Typefinancement(models.Model):
    idtypefinancement=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=70)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idnaturetache=models.ForeignKey(Naturetache, on_delete=models.CASCADE, null=True, db_column='idnaturetache')
    class Meta:
        db_table = 'typefinancement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Soussecteur(models.Model):
    idsoussecteur=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=70)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idsecteur=models.ForeignKey(Secteur, on_delete=models.CASCADE, null=True, db_column='idsecteur')
    class Meta:
        db_table = 'soussecteur'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Institution(models.Model):
    idinstitution=models.AutoField(primary_key=True, null=False)
    nom=models.CharField(max_length=70)
    code=models.CharField(max_length=50)
    choixstrategique=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    sigle=models.CharField(max_length=50)
    chapitre=models.CharField(max_length=50,null=True) 
    nom_en=models.CharField(max_length=50)
    idsoussecteur=models.ForeignKey(Soussecteur, on_delete=models.CASCADE, null=True, db_column='idsoussecteur')
    class Meta:
        db_table = 'institution'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Pyramide(models.Model):
    idpyramide=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=70)
    superficie=models.CharField(max_length=50)
    population=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idniveaupyramide=models.ForeignKey(Niveaupyramide, on_delete=models.CASCADE, null=True, db_column='idniveaupyramide')
    class Meta:
        db_table = 'pyramide'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Statutstructure(models.Model):
    idstatutstructure=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'statutstructure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Structure(models.Model):
    idstructure=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=50)
    article=models.CharField(max_length=50)
    nomrespo=models.CharField(max_length=50)
    arretecreation=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    cordonex=models.CharField(max_length=50)
    cordoney=models.CharField(max_length=50)
    presentation=models.CharField(max_length=50)
    pap=models.CharField(max_length=50)
    actif=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    dateouverture=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    vision=models.CharField(max_length=50)
    axeintervention=models.CharField(max_length=50)
    objectifgeneral=models.CharField(max_length=50)
    objectifspecifique=models.CharField(max_length=50)
    idarrondissement=models.ForeignKey(Arrondissement, on_delete=models.CASCADE, null=True, db_column='idarrondissement')
    idtypestructure=models.ForeignKey(Typestructure, on_delete=models.CASCADE, null=True, db_column='idtypestructure')
    id_adresse=models.ForeignKey(Adresse, on_delete=models.CASCADE, null=True, db_column='id_adresse')
    iddepartement=models.ForeignKey(Departement, on_delete=models.CASCADE, null=True, db_column='iddepartement')
    idstatutstructure=models.ForeignKey(Statutstructure, on_delete=models.CASCADE, null=True, db_column='idstatutstructure')
    idniveaupyramide=models.ForeignKey(Niveaupyramide, on_delete=models.CASCADE, null=True, db_column='idniveaupyramide')
    idpyramide=models.ForeignKey(Pyramide, on_delete=models.CASCADE, null=True, db_column='idpyramide')
    idregion=models.ForeignKey(Region, on_delete=models.CASCADE, null=True, db_column='idregion')
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, db_column='idinstitution')
    idrattachement=models.ForeignKey(Rattachement, on_delete=models.CASCADE, null=True, db_column='idrattachement')
    class Meta:
        db_table = 'structure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Section(models.Model):
    idsection=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    idarticle=models.ForeignKey(Article, on_delete=models.CASCADE, null=True, db_column='idarticle')
    class Meta:
        db_table = 'section'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Periode(models.Model):
    idperiode=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    idfrequence=models.ForeignKey(Frequence, on_delete=models.CASCADE, null=True, db_column='idfrequence')
    class Meta:
        db_table = 'periode'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Souscritere(models.Model):
    idsouscritere=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    detail=models.CharField(max_length=50)
    service=models.CharField(max_length=50)
    personel=models.CharField(max_length=50)
    idcomposante=models.ForeignKey(Composante, on_delete=models.CASCADE, null=True, db_column='idcomposante')
    idcritere=models.ForeignKey(Critere, on_delete=models.CASCADE, null=True, db_column='idcritere')
    class Meta:
        db_table = 'souscritere'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Programme(models.Model):
    idprogramme=models.AutoField(primary_key=True,null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    stratrgieprogramme=models.CharField(max_length=50)
    respomeo=models.CharField(max_length=50)
    cadremeo=models.CharField(max_length=50)
    impact=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    objectifs=models.CharField(max_length=50)
    objectifstrategique=models.CharField(max_length=50)
    fonction=models.CharField(max_length=50)
    indicateur=models.CharField(max_length=50)
    baseline=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    idsoussecteur=models.ForeignKey(Soussecteur, on_delete=models.CASCADE, null=True, db_column='idsoussecteur')
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, db_column='idinstitution')
    idaxestrategique=models.ForeignKey(Axestrategique, on_delete=models.CASCADE, null=True, db_column='idaxestrategique')
    class Meta:
        db_table = 'programme'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Mission(models.Model):
    idmission=models.CharField(primary_key=True, null=False)
    code=models.CharField(max_length=50)
    problemes=models.CharField(max_length=50)
    objectgeneral=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    objectspecifique=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    objectifs=models.CharField(max_length=50)
    objectifstrategique=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    idniveaupyramide=models.ForeignKey(Niveaupyramide, on_delete=models.CASCADE, null=True, db_column='idniveaupyramide')
    idbasejuridique=models.ForeignKey(Basejuridique, on_delete=models.CASCADE, null=True, db_column='idbasejuridique')
    class Meta:
        db_table = 'mission'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Detailsc(models.Model):
    iddetailsc=models.CharField(primary_key=True, null=False)
    pointmax=models.CharField(max_length=50)
    detail=models.CharField(max_length=50)
    problemes=models.CharField(max_length=50)
    objectif=models.CharField(max_length=50)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idsouscritere=models.ForeignKey(Souscritere, on_delete=models.CASCADE, null=True, db_column='idsouscritere')
    idmission=models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, db_column='idmission')
    class Meta:
        db_table = 'detailsc'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Budget(models.Model):
    idbudget=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    annee=models.CharField(max_length=50)
    class Meta:
        db_table = 'budget'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Annee(models.Model):
    idannee=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    choix=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    budget=models.CharField(max_length=50)
    defaut=models.CharField(max_length=50)
    fc=models.CharField(max_length=50)
    class Meta:
        db_table = 'annee'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    

class Evaluationstructure(models.Model):
    idevaluationstructure=models.CharField(primary_key=True, null=False)
    score_periode_prec=models.CharField(max_length=50)
    score_periode_actuel_previ=models.CharField(max_length=50)
    score_periode_actuel_real=models.CharField(max_length=50)
    applicable=models.CharField(max_length=50)
    probleme=models.CharField(max_length=50)
    iddetailsc=models.ForeignKey(Detailsc, on_delete=models.CASCADE, null=True, db_column='iddetailsc')
    periode_id=models.ForeignKey(Periode, on_delete=models.CASCADE, null=True, db_column='periode_id')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, db_column='idbudget')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    class Meta:
        db_table = 'evaluationstructure'  # Specify the exact table name you want

    
class Sousrubrique(models.Model):
    idsousrubrique=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    idrubrique=models.ForeignKey(Rubrique, on_delete=models.CASCADE, null=True, db_column='idrubrique')
    class Meta:
        db_table = 'sousrubrique'  

    def __str__(self):
        return self.nom

class Rubriquemercurial(models.Model):
    idrubriquemercurial=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    class Meta:
        db_table = 'rubriquemercurial'  

    def __str__(self):
        return self.nom


class Sousrubriquemercurial(models.Model):
    idsousrubriquemercurial=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    idrubriquemercurial=models.ForeignKey(Rubriquemercurial, on_delete=models.CASCADE, null=True, db_column='idrubriquemercurial')
    class Meta:
        db_table = 'sousrubriquemercurial'  

    def __str__(self):
        return self.nom

class Groupe_utilisateur(models.Model):
    idgroupe_utilisateur=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'groupe_utilisateur'  

    def __str__(self):
        return self.nom

class compteinstitution(models.Model):
    idcompteinstitution=models.CharField(primary_key=True, null=False)
    defaut=models.CharField(max_length=50)
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, db_column='idinstitution')
    idcompte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True, db_column='idcompte')
    class Meta:
        db_table = 'compteinstitution'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Indicateurprogramme(models.Model):
    idindicateurprogramme=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=100)
    objectif=models.CharField(max_length=50)
    periodicitecollecte=models.CharField(max_length=50)
    moyens=models.CharField(max_length=50)
    difficultes=models.CharField(max_length=50)
    pap=models.CharField(max_length=50)
    coefmulti=models.CharField(max_length=50)
    sourcedonnees=models.CharField(max_length=50)
    modecalcul=models.CharField(max_length=50)
    denominateur=models.CharField(max_length=50)
    numerateur=models.CharField(max_length=50)
    sourceverification=models.CharField(max_length=50)
    reference=models.CharField(max_length=50)
    annebaseline=models.CharField(max_length=50)
    annecible=models.CharField(max_length=50)
    unite=models.CharField(max_length=50)
    pourcentage=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    basline=models.CharField(max_length=50)
    valeurrealise=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    actif=models.CharField(max_length=50)
    periodicitemesure=models.CharField(max_length=50)
    commentaire=models.CharField(max_length=50)
    interpretation=models.CharField(max_length=50)
    limite=models.CharField(max_length=50)
    analyse=models.CharField(max_length=50)
    serviceanalyse=models.CharField(max_length=50)
    servicesynthese=models.CharField(max_length=50)
    servicevalidation=models.CharField(max_length=50)
    servicerespo=models.CharField(max_length=50)
    modecollecte=models.CharField(max_length=50)
    explication=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True, db_column='idtypedonnees')
    class Meta:
        db_table = 'indicateurprogramme'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Action(models.Model):
    idaction=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    effet=models.CharField(max_length=50)
    cadremeo=models.CharField(max_length=50)
    respomeo=models.CharField(max_length=50)
    objectifs=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    indicateur=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    idzone=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, db_column='idzone')
    idindicateurprogramme=models.ForeignKey(Indicateurprogramme, on_delete=models.CASCADE, null=True, db_column='idindicateurprogramme')
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    class Meta:
        db_table = 'action'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Indicateuraction(models.Model):
    idindicateuraction=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=100)
    objectif=models.CharField(max_length=50)
    periodicitecollecte=models.CharField(max_length=50)
    moyens=models.CharField(max_length=50)
    difficultes=models.CharField(max_length=50)
    pap=models.CharField(max_length=50)
    coefmulti=models.CharField(max_length=50)
    sourcedonnees=models.CharField(max_length=50)
    modecalcul=models.CharField(max_length=50)
    denominateur=models.CharField(max_length=50)
    numerateur=models.CharField(max_length=50)
    sourceverification=models.CharField(max_length=50)
    reference=models.CharField(max_length=50)
    annebaseline=models.CharField(max_length=50)
    annecible=models.CharField(max_length=50)
    unite=models.CharField(max_length=50)
    pourcentage=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    basline=models.CharField(max_length=50)
    valeurrealise=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    actif=models.CharField(max_length=50)
    periodicitemesure=models.CharField(max_length=50)
    commentaire=models.CharField(max_length=50)
    interpretation=models.CharField(max_length=50)
    limite=models.CharField(max_length=50)
    analyse=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    coutcollecte=models.CharField(max_length=50)
    serviceanalyse=models.CharField(max_length=50)
    servicesynthese=models.CharField(max_length=50)
    servicevalidation=models.CharField(max_length=50)
    servicerespo=models.CharField(max_length=50)
    modecollecte=models.CharField(max_length=50)
    explication=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True, db_column='idtypedonnees')
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True, db_column='idaction')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    class Meta:
        db_table = 'indicateuraction'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Activite(models.Model):
    idactivite=models.AutoField(primary_key=True,null=False)
    nom=models.CharField(max_length=100)
    code=models.CharField(max_length=50)
    objectif=models.CharField(max_length=50)
    prio=models.BooleanField(max_length=50)
    partisprenantes=models.CharField(max_length=50)
    autreconcerne=models.CharField(max_length=50)
    cumulextrants=models.CharField(max_length=50)
    responsables=models.CharField(max_length=50)
    justification=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    cumulindicateurs=models.CharField(max_length=50)
    idstructure=models.ForeignKey(Structure, null=True, db_column='idstructure',on_delete=models.CASCADE)
    idaction=models.ForeignKey(Action, null=True, db_column='idaction',on_delete=models.CASCADE)
    idannee=models.ForeignKey(Annee,  null=True, db_column='idannee',on_delete=models.CASCADE)
    idindicateuraction=models.ForeignKey(Indicateuraction,  null=True, db_column='idindicateuraction',on_delete=models.CASCADE)
    idtypeactivite=models.ForeignKey(Typeactivite,  null=True, db_column='idtypeactivite',on_delete=models.CASCADE)
    idrang=models.ForeignKey(Rang,  null=True, db_column='idrang',on_delete=models.CASCADE)
    class Meta:
        db_table = 'activite'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

    
class Tache(models.Model):
    idtache=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=100)
    numordre=models.CharField(max_length=50)
    totalmontantaloue=models.CharField(max_length=50)
    moyensnecessaires=models.CharField(max_length=50)
    indicateurs2014=models.CharField(max_length=50)
    aeencours=models.CharField(max_length=50)
    cpconsommee=models.CharField(max_length=50)
    indicateurspoursuivis=models.CharField(max_length=50)
    valider=models.CharField(max_length=50)
    m1=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    m2=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    periodeexecution=models.CharField(max_length=50)
    montantengage=models.CharField(max_length=50)
    montantliquide=models.CharField(max_length=50)
    montantpayeht=models.CharField(max_length=50)
    montantpayettc=models.CharField(max_length=50)
    resultprocess=models.CharField(max_length=50)
    indicateurresult=models.CharField(max_length=50)
    montant_ordonne=models.CharField(max_length=50)
    taxe_ordonne=models.CharField(max_length=75)
    nap_ordonne=models.CharField(max_length=50)
    valeurattendue=models.CharField(max_length=50)
    justification=models.CharField(max_length=50)
    valeurrealisee=models.CharField(max_length=50)
    cpanneeplus1=models.CharField(max_length=50)
    cpanneeplus2=models.CharField(max_length=50)
    m3=models.CharField(max_length=50)
    m4=models.CharField(max_length=50)
    m5=models.CharField(max_length=50)
    m6=models.CharField(max_length=50)
    m7=models.CharField(max_length=50)
    m8=models.CharField(max_length=50)
    m9=models.CharField(max_length=50)
    m10=models.CharField(max_length=50)
    m11=models.CharField(max_length=50)
    m12=models.CharField(max_length=50)
    idevaluationstructure=models.ForeignKey(Evaluationstructure, on_delete=models.CASCADE, null=True, db_column='idevaluationstructure')
    periode_id=models.ForeignKey(Periode, on_delete=models.CASCADE, null=True, db_column='periode_id')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    idnaturetache=models.ForeignKey(Naturetache, on_delete=models.CASCADE, null=True, db_column='idnaturetache')
    idnature_t=models.ForeignKey(Nature_t, on_delete=models.CASCADE, null=True, db_column='idnature_t')
    idbailleurfond=models.ForeignKey(Bailleurfond, on_delete=models.CASCADE, null=True, db_column='idbailleurfond')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idrisque=models.ForeignKey(Risque, on_delete=models.CASCADE, null=True, db_column='idrisque')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
    idtypefinancement=models.ForeignKey(Typefinancement, on_delete=models.CASCADE, null=True, db_column='idtypefinancement')
    class Meta:
        db_table = 'tache'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Cpte_grpusers(models.Model):
    idcpte_grpusers=models.CharField(primary_key=True, null=False)
    idcompte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True, db_column='idcompte')
    id_groupe_utilisateur=models.ForeignKey(Groupe_utilisateur, on_delete=models.CASCADE, null=True, db_column='id_groupe_utilisateur')
    class Meta:
        db_table = 'cpte_grpusers'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Imputation(models.Model):
    idimputation=models.CharField(primary_key=True, null=False)
    code=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idsousrubrique=models.ForeignKey(Sousrubrique, on_delete=models.CASCADE, null=True, db_column='idsousrubrique')
    idsection=models.ForeignKey(Section, on_delete=models.CASCADE, null=True, db_column='idsection')
    idsousrubriquemercurial=models.ForeignKey(Sousrubriquemercurial, on_delete=models.CASCADE, null=True, db_column='idsousrubriquemercurial')
    idtypeimputation=models.ForeignKey(Typeimputation, on_delete=models.CASCADE, null=True, db_column='idtypeimputation')
    class Meta:
        db_table = 'imputation'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Moyens(models.Model):
    idmoyens=models.CharField(primary_key=True, null=False)
    cp=models.CharField(max_length=50)
    ct=models.CharField(max_length=50)
    cu=models.CharField(max_length=50)
    qte=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    montantexecute=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregitre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    quantie=models.CharField(max_length=50)
    cpanneeplus1=models.CharField(max_length=50)
    cpanneeplus2=models.CharField(max_length=50)
    montant_paye=models.CharField(max_length=50)
    montant_ordonne=models.CharField(max_length=50)
    taxe_ordonne=models.CharField(max_length=50)
    nap_ordonne=models.CharField(max_length=50)
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, db_column='idbudget')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True, db_column='idimputation')
    class Meta:
        db_table = 'moyens'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Indicateurprogrammeannee(models.Model):
    idindicateurprogrrammeannee=models.CharField(primary_key=True, null=False)
    date_enregitre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    valeurintermediaire=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    basline=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    unite=models.CharField(max_length=50)
    annebaseline=models.CharField(max_length=50)
    annecible=models.CharField(max_length=50)
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    idindicateurprogramme=models.ForeignKey(Indicateurprogramme, on_delete=models.CASCADE, null=True, db_column='idindicateurprogramme')
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True, db_column='idtypedonnees')
    class Meta:
        db_table = 'indicateurprogrammeannee'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Societe(models.Model):
    idsociete=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=100)
    ad1=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    coge=models.CharField(max_length=50)
    auxi=models.CharField(max_length=50)
    ad2=models.CharField(max_length=50)
    ad3=models.CharField(max_length=50)
    pays=models.CharField(max_length=50)
    tel=models.CharField(max_length=50)
    fax=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    rib1=models.CharField(max_length=50)
    rib2=models.CharField(max_length=50)
    dom1=models.CharField(max_length=50)
    dom2=models.CharField(max_length=50)
    nbjours=models.CharField(max_length=50)
    jourref=models.CharField(max_length=50)
    cogeconsolide=models.CharField(max_length=50)
    auxiconsolide=models.CharField(max_length=50)
    datecre=models.CharField(max_length=50)
    datemaj=models.CharField(max_length=50)
    usecre=models.CharField(max_length=50)
    usermaj=models.CharField(max_length=50)
    planconsolide=models.CharField(max_length=50)
    statut=models.CharField(max_length=50)
    rc=models.CharField(max_length=50)
    nif=models.CharField(max_length=50)
    stat=models.CharField(max_length=50)
    bqnom=models.CharField(max_length=50)
    bqville=models.CharField(max_length=50)
    bqpays=models.CharField(max_length=50)
    bqswift=models.CharField(max_length=50)
    class Meta:
        db_table = 'societe'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Signataire(models.Model):
    idsignataire=models.CharField(primary_key=True, null=False)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)
    class Meta:
        db_table = 'signataire'  

    def __str__(self):
        return self.nom
    
class Boncommande(models.Model):
    idboncommande=models.CharField(primary_key=True, null=False)
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True, db_column='idimputation')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idsociete=models.ForeignKey(Societe, on_delete=models.CASCADE, null=True, db_column='idsociete')
    idsignataire=models.ForeignKey(Signataire, on_delete=models.CASCADE, null=True, db_column='idsignataire')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, db_column='idbudget')
    idmoyens=models.ForeignKey(Moyens, on_delete=models.CASCADE, null=True, db_column='idmoyens')
    dateemission=models.CharField(max_length=100)
    object=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    delailivraison=models.CharField(max_length=50)
    totalht=models.CharField(max_length=50)
    tva=models.CharField(max_length=50)
    totalair=models.CharField(max_length=50)
    netapayer=models.CharField(max_length=50)
    avance=models.CharField(max_length=50)
    montantenlettre=models.CharField(max_length=50)
    ttc=models.CharField(max_length=50)
    espece=models.CharField(max_length=50)
    cheque=models.CharField(max_length=50)
    virement=models.CharField(max_length=50)
    datelivraison=models.CharField(max_length=50)
    engage=models.CharField(max_length=50)
    tauxtva=models.CharField(max_length=50)
    tauxair=models.CharField(max_length=50)
    reference=models.CharField(max_length=50)
    imputations=models.CharField(max_length=50)
    coefficientreducteur=models.CharField(max_length=50)
    verif=models.CharField(max_length=50)
    valide=models.CharField(max_length=50)
    nombreverif=models.CharField(max_length=50)
    bc=models.CharField(max_length=50)
    lettrecommande=models.CharField(max_length=50)
    mission=models.CharField(max_length=50)
    gre_a_gre=models.CharField(max_length=50)
    attentepayement=models.CharField(max_length=50)
    paye=models.CharField(max_length=50)
    liquide=models.CharField(max_length=50)
    montant_paye=models.CharField(max_length=50)
    salaire=models.CharField(max_length=50)
    mmontant_ordonne=models.CharField(max_length=50)
    taxe_ordonne=models.CharField(max_length=50)
    nap_ordonne=models.CharField(max_length=50)
    class Meta:
        db_table = 'boncommande'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Criterestructure(models.Model):
    idcriterestructure=models.CharField(primary_key=True, null=False)
    poids=models.CharField(max_length=50)
    point_max=models.CharField(max_length=50)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idcritere=models.ForeignKey(Critere, on_delete=models.CASCADE, null=True, db_column='idcritere')
    class Meta:
        db_table = 'criterestructure'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Structuremission(models.Model):
    idstucturemission=models.CharField(primary_key=True, null=False)
    problemes=models.CharField(max_length=50)
    objectif=models.CharField(max_length=50)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idmission=models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, db_column='idmission')
    class Meta:
        db_table = 'structuremission'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Tacheindicateurperformance(models.Model):
    idtacheindicateurperformance=models.CharField(primary_key=True, null=False)
    cout=models.CharField(max_length=50)
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    class Meta:
        db_table = 'tacheindicateurperformance'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Typeperiode(models.Model):
    idtypeperiode=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    defaut=models.CharField(max_length=50)
    parent_id=models.ForeignKey(Parent, on_delete=models.CASCADE, null=True, db_column='parent_id')
    class Meta:
        db_table = 'typeperiode'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Action1(models.Model):
    idaction1=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    effet=models.CharField(max_length=50)
    cadremeo=models.CharField(max_length=50)
    respomeo=models.CharField(max_length=50)
    objectifs=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    indicateur=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    basline=models.CharField(max_length=50)
    idzone=models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, db_column='idzone')
    idindicateurprogramme=models.ForeignKey(Indicateurprogramme, on_delete=models.CASCADE, null=True, db_column='idindicateurprogramme')
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True, db_column='idaction')
    class Meta:
        db_table = 'action1'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Structuremissionactivite(models.Model):
    idstructuremissionactivite=models.CharField(primary_key=True, null=False)
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
    objectif=models.CharField(max_length=50)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idmission=models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, db_column='idmission')
    class Meta:
        db_table = 'structuremissionactivite'  # Specify the exact table name you want

    def __str__(self):
        return self.nom
    
class Tachebon(models.Model):
    idtachebon=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=100)
    numordre=models.CharField(max_length=50)
    totalmonatntaloue=models.CharField(max_length=50)
    moyennecessaire=models.CharField(max_length=50)
    indicateur2014=models.CharField(max_length=50)
    aeencors=models.CharField(max_length=50)
    cpconsomee=models.CharField(max_length=50)
    indicateurpoursuivis=models.CharField(max_length=50)
    valider=models.CharField(max_length=50)
    m1=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    m2=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    m3=models.CharField(max_length=50)
    m4=models.CharField(max_length=50)
    m5=models.CharField(max_length=50)
    m6=models.CharField(max_length=50)
    m7=models.CharField(max_length=50)
    m8=models.CharField(max_length=50)
    m9=models.CharField(max_length=50)
    m10=models.CharField(max_length=50)
    m11=models.CharField(max_length=50)
    m12=models.CharField(max_length=50)
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
    idtypefinancement=models.ForeignKey(Typefinancement, on_delete=models.CASCADE, null=True, db_column='idtypefinancement')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idrisque=models.ForeignKey(Risque, on_delete=models.CASCADE, null=True, db_column='idrisque')
    idbailleurfond=models.ForeignKey(Bailleurfond, on_delete=models.CASCADE, null=True, db_column='idbailleurfond')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    idnature_t=models.ForeignKey(Nature_t, on_delete=models.CASCADE, null=True, db_column='idnature_t')
    idnaturetache=models.ForeignKey(Naturetache, on_delete=models.CASCADE, null=True, db_column='idnaturetache')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    class Meta:
        db_table = 'tachebon'  

    def __str__(self):
        return self.nom

class Utilisateurstructure(models.Model):
    idutilisateurstructure=models.CharField(primary_key=True, null=False)
    id_utilisateur=models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, db_column='id_utilisateur')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    class Meta:
        db_table = 'utilisateurstructure'  

    def __str__(self):
        return self.nom

class  Verificationbc(models.Model):
    idverificationbc=models.CharField(primary_key=True, null=False)
    dateverification=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    valide=models.CharField(max_length=50)
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True, db_column='idboncommande')
    class Meta:
        db_table = 'verificationbc'  

    def __str__(self):
        return self.nom

class Activitestructure(models.Model):
    idactivitestructure=models.CharField(primary_key=True, null=False)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
    class Meta:
        db_table = 'activitestructure'  

    def __str__(self):
        return self.nom

class Activitetypestructure(models.Model):
     idactivitetypestructure=models.CharField(primary_key=True, null=False)
     idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
     strategies=models.CharField(max_length=50)
     objectif=models.CharField(max_length=50)
     class Meta:
        db_table = 'activitetypestructure'  

     def __str__(self):
        return self.nom

class Personnel(models.Model):
    idpersonnel=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=100)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    class Meta:
        db_table = 'personnel'  

    def __str__(self):
        return self.nom

class Activitecorrectrices(models.Model):
    idactivitecorrectrice=models.CharField(primary_key=True, null=False)
    operation=models.CharField(max_length=50)
    montant=models.CharField(max_length=50)
    niveau=models.CharField(max_length=50)
    created_at=models.CharField(max_length=50)
    updated_at=models.CharField(max_length=50)
    statut=models.CharField(max_length=50)
    periode_id=models.ForeignKey(Periode, on_delete=models.CASCADE, null=True, db_column='periode_id')
    tache_id=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='tache_id')
    idpersonnel=models.ForeignKey(Personnel, on_delete=models.CASCADE, null=True, db_column='idpersonnel')
    class Meta:
        db_table = 'activitecorrectrices'  

    def __str__(self):
        return self.nom

class Methodeeval(models.Model):
    idmethodeeval=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'methodeeval'  

    def __str__(self):
        return self.nom

class Origineindicateur(models.Model):
    idorigineindicateur=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'origineindicateur'  

    def __str__(self):
        return self.nom


class Indicateurperformance(models.Model):
    idindicateurperformance=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=100)
    periodicitecollecte=models.CharField(max_length=50)
    moyens=models.CharField(max_length=50)
    difficultes=models.CharField(max_length=50)
    pap=models.CharField(max_length=50)
    coefmulti=models.CharField(max_length=50)
    sourcedonnees=models.CharField(max_length=50)
    modecalcul=models.CharField(max_length=50)
    denominateur=models.CharField(max_length=50)
    numerateur=models.CharField(max_length=50)
    sourceverification=models.CharField(max_length=50)
    reference=models.CharField(max_length=50)
    annebaseline=models.CharField(max_length=50)
    annecible=models.CharField(max_length=50)
    unite=models.CharField(max_length=50)
    pourcentage=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    basline=models.CharField(max_length=50)
    valeurrealise=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    actif=models.CharField(max_length=50)
    periodicitemesure=models.CharField(max_length=50)
    commentaire=models.CharField(max_length=50)
    interpretation=models.CharField(max_length=50)
    limite=models.CharField(max_length=50)
    analyse=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    coutcollecte=models.CharField(max_length=50)
    serviceanalyse=models.CharField(max_length=50)
    servicesynthese=models.CharField(max_length=50)
    servicevalidation=models.CharField(max_length=50)
    servicerespo=models.CharField(max_length=50)
    modecollecte=models.CharField(max_length=50)
    explication=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True, db_column='idtypedonnees')
    idniveaupyramide=models.ForeignKey(Niveaupyramide, on_delete=models.CASCADE, null=True, db_column='idaction')
    idorigineindicateur=models.ForeignKey(Origineindicateur, on_delete=models.CASCADE, null=True, db_column='idannee')
    class Meta:
        db_table = 'indicateurperformance'  

    def __str__(self):
        return self.nom


class Extrant(models.Model):
    idextrant=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    cout=models.CharField(max_length=50)
    indicateurs=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idmethodeeval=models.ForeignKey(Methodeeval, on_delete=models.CASCADE, null=True, db_column='idmethodeeval')
    idindicateurperformance=models.ForeignKey(Indicateurperformance, on_delete=models.CASCADE, null=True, db_column='idindicateurperformance')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
    class Meta:
        db_table = 'extrant'  

    def __str__(self):
        return self.nom


class Importextrant(models.Model):
    idimportextrant=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    idextrant=models.ForeignKey(Extrant, on_delete=models.CASCADE, null=True, db_column='idextrant')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
    class Meta:
        db_table = 'importextrant'  

    def __str__(self):
        return self.nom
    
class Elementcout(models.Model):
    idelementcout=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    prixunitaire=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True, db_column='idimputation')
    idrubriquemercurial=models.ForeignKey(Rubriquemercurial, on_delete=models.CASCADE, null=True, db_column='idrubriquemercuriale')
    idunite=models.ForeignKey(Unite, on_delete=models.CASCADE, null=True, db_column='idunite')
    idsousrubriquemercurial=models.ForeignKey(Sousrubriquemercurial, on_delete=models.CASCADE, null=True, db_column='idsousrubriquemercurial')
    class Meta:
        db_table = 'elementcout'  

    def __str__(self):
        return self.nom

class Exercice(models.Model):
    idexercise=models.CharField(primary_key=True, null=False)
    coutglobal=models.CharField(max_length=50)
    nom_exercice=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    montantaccorde=models.CharField(max_length=50)
    ispublicpropbudgetsante=models.CharField(max_length=50)
    montantreel=models.CharField(max_length=50)
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, db_column='idinstitution')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    class Meta:
        db_table = 'exercice'  

    def __str__(self):
        return self.nom

class Exercise_action(models.Model):
    idexercise_action=models.CharField(primary_key=True, null=False)
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True, db_column='idaction')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True, db_column='idexercice')
    tauxacceptable=models.CharField(max_length=50)
    coutprogaction=models.CharField(max_length=50)
    poidaction=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'exercice_action'  

    def __str__(self):
        return self.nom

class Exercice_nature(models.Model):
    idexercise_nature=models.CharField(primary_key=True, null=False)
    montant=models.CharField(max_length=50)
    pourcentage=models.CharField(max_length=50)
    idnature_t=models.ForeignKey(Nature_t, on_delete=models.CASCADE, null=True, db_column='idnature_t')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True, db_column='idexercice')
    class Meta:
        db_table = 'exercice_nature'  

    def __str__(self):
        return self.nom


class Exercicenature_t(models.Model):
    idexercisenature_t=models.CharField(primary_key=True, null=False)
    montant=models.CharField(max_length=50)
    pourcentage=models.CharField(max_length=50)
    idnature_t=models.ForeignKey(Nature_t, on_delete=models.CASCADE, null=True, db_column='idnature_t')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True, db_column='idexercice')
    class Meta:
        db_table = 'exercicenature_t'  

    def __str__(self):
        return self.nom

class Exercicetypefinancement(models.Model):
    idexercisetypefinancement=models.CharField(primary_key=True, null=False)
    montant=models.CharField(max_length=50)
    pourcentage=models.CharField(max_length=50)
    idtypefinancement=models.ForeignKey(Typefinancement, on_delete=models.CASCADE, null=True, db_column='idtypefinancement')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True, db_column='idexercice')
    class Meta:
        db_table = 'exercicetypefinancement'  

    def __str__(self):
        return self.nom

class Exercise_programme(models.Model):
    idexercise_programme=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    coutprog=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    idexercice=models.ForeignKey(Exercice, on_delete=models.CASCADE, null=True, db_column='idexercice')
    class Meta:
        db_table = 'exercice_programme'  

    def __str__(self):
        return self.nom
class Ordre_payement(models.Model):
     idordre_payement=models.CharField(primary_key=True, null=False)
     beneficiaire=models.CharField(max_length=50)
     montant=models.CharField(max_length=50)
     taxe=models.CharField(max_length=50)
     nap=models.CharField(max_length=50)
     montant_en_lettre=models.CharField(max_length=50)
     detail_nap=models.CharField(max_length=50)
     detail_tva=models.CharField(max_length=50)
     detail_air=models.CharField(max_length=50)
     pieces=models.CharField(max_length=50)
     etat=models.CharField(max_length=50)
     code=models.CharField(max_length=50)
     objet=models.CharField(max_length=50)
     mode_paiement=models.CharField(max_length=50)
     nombre_verification=models.CharField(max_length=50)
     pays=models.CharField(max_length=50) 
     date_ordonnation=models.CharField(max_length=50)
     idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True, db_column='idboncommande')
     class Meta:
        db_table = 'ordre_payement'  

     def __str__(self):
        return self.nom

class Verifiaction_op(models.Model):
    idverification_op=models.CharField(primary_key=True, null=False)
    date_verification=models.CharField(max_length=50)
    valide=models.CharField(max_length=50)
    idordre_payement=models.ForeignKey(Ordre_payement, on_delete=models.CASCADE, null=True, db_column='idordre_payement')
    class Meta:
        db_table = 'verification_op'  

    def __str__(self):
        return self.nom

class Ligne_decision(models.Model):
    idligne_decision=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    coutunitaire=models.CharField(max_length=50)
    quantite=models.CharField(max_length=50)
    total=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    verif=models.CharField(max_length=50)
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True, db_column='idboncommande')
    class Meta:
        db_table = 'ligne_decision'  

    def __str__(self):
        return self.nom

class Ligneboncommande(models.Model):
    idligneboncommande=models.CharField(primary_key=True, null=False)
    prixunitaire=models.CharField(max_length=50)
    quantite=models.CharField(max_length=50)
    total=models.CharField(max_length=50)
    prixmercurial=models.CharField(max_length=50)
    verif=models.CharField(max_length=50)
    references=models.CharField(max_length=50)
    idelementcout=models.ForeignKey(Elementcout, on_delete=models.CASCADE, null=True, db_column='idelementcout')
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True, db_column='idboncommande')
    class Meta:
        db_table = 'ligneboncommande'  

    def __str__(self):
        return self.nom

class Ligne_verification_bc(models.Model):
    idligne_verifiaction_bc=models.CharField(primary_key=True, null=False)
    idverificationbc=models.ForeignKey(Verificationbc, on_delete=models.CASCADE, null=True, db_column='idverificationbc')
    idligne_decision=models.ForeignKey(Ligne_decision, on_delete=models.CASCADE, null=True, db_column='idligne_decision')
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True, db_column='idboncommande')
    class Meta:
        db_table = 'ligne_verification_bc'  

    def __str__(self):
        return self.nom

class Menu(models.Model):
    idmenu=models.CharField(primary_key=True, null=False)
    name=models.CharField(max_length=50)
    libelle=models.CharField(max_length=50)
    shortcut=models.CharField(max_length=50)
    categorie=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    id_parent=models.ForeignKey(Parent, on_delete=models.CASCADE, null=True, db_column='id_parent')
    class Meta:
        db_table = 'menu'  

    def __str__(self):
        return self.nom

class Recette(models.Model):
    idrecette=models.CharField(primary_key=True, null=False)
    ranneeavant=models.CharField(max_length=50)
    reaaneeavant=models.CharField(max_length=50)
    prannee_plus_1_cout=models.CharField(max_length=50)
    prannee_plus_1_qte=models.CharField(max_length=50)
    prannee_plus_1_total=models.CharField(max_length=50)
    prannee_plus_2_cout=models.CharField(max_length=50)
    qte=models.CharField(max_length=50)
    cu=models.CharField(max_length=50)
    ct=models.CharField(max_length=50)
    prannee_plus_2_qte=models.CharField(max_length=50)
    prannee_plus_2_total=models.CharField(max_length=50)
    ranneeavant_qte=models.CharField(max_length=50)
    ranneeavant_cu=models.CharField(max_length=50)
    raneeavant_qte=models.CharField(max_length=50)
    montant_consomme_avant=models.CharField(max_length=50)
    reaanneeavant_cu=models.CharField(max_length=50)
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    idbailleurfond=models.ForeignKey(Bailleurfond, on_delete=models.CASCADE, null=True, db_column='idbailleurfond')
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True, db_column='idimputation')
    class Meta:
        db_table = 'recette'  

    def __str__(self):
        return self.nom

class Indicateuractivite(models.Model):
    idindicateuractivite=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=100)
    periodicitecollecte=models.CharField(max_length=50)
    moyens=models.CharField(max_length=50)
    difficultes=models.CharField(max_length=50)
    pap=models.CharField(max_length=50)
    coefmulti=models.CharField(max_length=50)
    sourcedonnees=models.CharField(max_length=50)
    modecalcul=models.CharField(max_length=50)
    denominateur=models.CharField(max_length=50)
    numerateur=models.CharField(max_length=50)
    sourceverification=models.CharField(max_length=50)
    reference=models.CharField(max_length=50)
    annebaseline=models.CharField(max_length=50)
    annecible=models.CharField(max_length=50)
    unite=models.CharField(max_length=50)
    pourcentage=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    basline=models.CharField(max_length=50)
    valeurrealise=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    actif=models.CharField(max_length=50)
    periodicitemesure=models.CharField(max_length=50)
    commentaire=models.CharField(max_length=50)
    interpretation=models.CharField(max_length=50)
    limite=models.CharField(max_length=50)
    analyse=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    coutcollecte=models.CharField(max_length=50)
    serviceanalyse=models.CharField(max_length=50)
    servicesynthese=models.CharField(max_length=50)
    servicevalidation=models.CharField(max_length=50)
    servicerespo=models.CharField(max_length=50)
    modecollecte=models.CharField(max_length=50)
    explication=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    hypothese_risque=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    idactvite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
    idtypedonnees=models.ForeignKey(Typedonnees, on_delete=models.CASCADE, null=True, db_column='idtypedonnees')
    class Meta:
        db_table = 'indicateuractivite'  

    def __str__(self):
        return self.nom

class Mois(models.Model):
    idmois=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    rang=models.CharField(max_length=50)
    choix=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'mois'  

    def __str__(self):
        return self.nom

class Semaine(models.Model):
    idsemaine=models.CharField(primary_key=True, null=False)
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    idmois=models.ForeignKey(Mois, on_delete=models.CASCADE, null=True, db_column='idmois')
    s4=models.CharField(max_length=50)
    s3=models.CharField(max_length=50)
    s2=models.CharField(max_length=50)
    s1=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    class Meta:
        db_table = 'semaine'  

    def __str__(self):
        return self.nom

class Moyens1(models.Model):
    idmoyens1=models.CharField(primary_key=True, null=False)
    cp=models.CharField(max_length=50)
    ct=models.CharField(max_length=50)
    cu=models.CharField(max_length=50)
    qte=models.CharField(max_length=50)
    montantexecute=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    quantite=models.CharField(max_length=50)
    cpanneeplus1=models.CharField(max_length=50)
    cpanneeplus2=models.CharField(max_length=50)
    idmoyens=models.ForeignKey(Moyens, on_delete=models.CASCADE, null=True, db_column='idmoyens')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, db_column='idbudget')
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True, db_column='idimputation')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    etat=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    class Meta:
        db_table = 'moyens1'  

    def __str__(self):
        return self.nom

class Moyensbon(models.Model):
    idmoyensbon=models.AutoField(primary_key=True, null=False)
    cp=models.CharField(max_length=50)
    ct=models.CharField(max_length=50)
    cu=models.CharField(max_length=50)
    qte=models.CharField(max_length=50)
    montantexecute=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    quantite=models.CharField(max_length=50)
    cpanneeplus1=models.CharField(max_length=50)
    cpanneeplus2=models.CharField(max_length=50)
    idmoyens=models.ForeignKey(Moyens, on_delete=models.CASCADE, null=True, db_column='idmoyens')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, db_column='idbudget')
    idimputation=models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True, db_column='idimputation')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    etat=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    class Meta:
        db_table = 'moyensbon'  

    def __str__(self):
        return self.nom
    
class Cdmt(models.Model):
    idcdmt=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    anneedebut=models.DateField(max_length=50)
    anneefin=models.DateField(max_length=50)
    class Meta:
        db_table = 'cdmt'  

    def __str__(self):
        return self.nom

class Budget_tache(models.Model):
    idbudget_tache=models.CharField(primary_key=True, null=False)
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    idbudget=models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, db_column='idbudget')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    idbailleurfond=models.ForeignKey(Bailleurfond, on_delete=models.CASCADE, null=True, db_column='idbailleurfond')
    idrisque=models.ForeignKey(Risque, on_delete=models.CASCADE, null=True, db_column='idrisque')
    class Meta:
        db_table = 'budget_tache'  

    def __str__(self):
        return self.nom


class Parametre(models.Model):
     idparametre=models.CharField(primary_key=True, null=False)
     idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True, db_column='idcdmt')
     class Meta:
        db_table = 'parametre'  

     def __str__(self):
        return self.nom

class Parametrage(models.Model):
    idparametrage=models.CharField(primary_key=True, null=False)
    tauxtva=models.CharField(max_length=100)
    tauxair=models.CharField(max_length=50)
    repertoire_photo=models.CharField(max_length=50)
    pourcentagemercurial=models.CharField(max_length=50)
    user_tompro=models.CharField(max_length=50)
    password_tompro=models.CharField(max_length=50)
    user_gendata=models.CharField(max_length=50)
    password_gendata=models.CharField(max_length=50)
    chaine_connexion_gendata=models.CharField(max_length=50)
    driver_class_name_gendata=models.CharField(max_length=50)
    data_base_name_tompro=models.CharField(max_length=50)
    driver_class_name_tompro=models.CharField(max_length=50)
    database_name_gendata=models.CharField(max_length=50)
    class Meta:
        db_table = 'parametrage'  

    def __str__(self):
        return self.nom
    
class Cdmt_annee(models.Model):
    idcdmt_annee=models.CharField(primary_key=True, null=False)
    idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True, db_column='idcdmt')
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    rang=models.CharField(max_length=50)
    class Meta:
        db_table = 'cdmt_annee'  

    def __str__(self):
        return self.nom

class Cdmt_tache(models.Model):
    idcdmt_tache=models.CharField(primary_key=True, null=False)
    ri1=models.CharField(max_length=50)
    ri2=models.CharField(max_length=100)
    ri3=models.CharField(max_length=50)
    re1=models.CharField(max_length=50)
    re2=models.CharField(max_length=50)
    re3=models.CharField(max_length=50)
    aeannee1=models.CharField(max_length=50)
    idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True, db_column='idcdmt')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    class Meta:
        db_table = 'cdmt_tache'  

    def __str__(self):
        return self.nom
    
class Cdmt_tachebon(models.Model):
    idcdmt_tachebon=models.CharField(primary_key=True, null=False)
    ri1=models.CharField(max_length=50)
    ri2=models.CharField(max_length=100)
    ri3=models.CharField(max_length=50)
    re1=models.CharField(max_length=50)
    re2=models.CharField(max_length=50)
    re3=models.CharField(max_length=50)
    aeannee1=models.CharField(max_length=50)
    idcdmt_tache=models.ForeignKey(Cdmt_tache, on_delete=models.CASCADE, null=True, db_column='idcdmt_tache')
    idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True, db_column='idcdmt')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    class Meta:
        db_table = 'cdmt_tachebon'  

    def __str__(self):
        return self.nom
    
class Cdmt_tacheok(models.Model):
    idcdmt_tacheok=models.CharField(primary_key=True, null=False)
    ri1=models.CharField(max_length=50)
    ri2=models.CharField(max_length=100)
    ri3=models.CharField(max_length=50)
    re1=models.CharField(max_length=50)
    re2=models.CharField(max_length=50)
    re3=models.CharField(max_length=50)
    aeannee1=models.CharField(max_length=50)
    idcdmt_tache=models.ForeignKey(Cdmt_tache, on_delete=models.CASCADE, null=True, db_column='idcdmt_tache')
    idcdmt=models.ForeignKey(Cdmt, on_delete=models.CASCADE, null=True, db_column='idcdmt')
    idtache=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='idtache')
    class Meta:
        db_table = 'cdmt_tacheok'  

    def __str__(self):
        return self.nom


class Certificatengagement(models.Model):
    idcertificatengagement=models.CharField(primary_key=True, null=False)
    idmoyens=models.ForeignKey(Moyens, on_delete=models.CASCADE, null=True, db_column='idmoyens')
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True, db_column='idboncommande')
    dateengagement=models.DateField(max_length=50)
    class Meta:
        db_table = 'certificatengagement'  

    def __str__(self):
        return self.nom
    

class Chronogrammes(models.Model):
    idchronogrammes=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    created_at=models.CharField(max_length=50)
    updated_at=models.CharField(max_length=50)
    periode_id=models.ForeignKey(Periode,  on_delete=models.CASCADE, null=True, db_column='periode_id')
    Activitecorrectrices_id=models.ForeignKey(Activitecorrectrices,  on_delete=models.CASCADE, null=True, db_column='activitecorrectrice_id')
    periodeparent_id=models.CharField(max_length=50)
    class Meta:
        db_table = 'chronogrammes'  

    def __str__(self):
        return self.nom
    
class Virement(models.Model):
    idvirement=models.AutoField(primary_key=True, null=False)
    
    nom = models.CharField(max_length=50)
    class Meta:
        db_table = 'virement'  # Specify the exact table name you want

    def __str__(self):
        return self.nom

class Payement(models.Model):
    idpayement=models.CharField(primary_key=True, null=False)
    ribbeneficiaire=models.CharField(max_length=50)
    code=models.CharField(max_length=100)
    reference=models.CharField(max_length=50)
    objet=models.CharField(max_length=50)
    montant=models.CharField(max_length=50)
    bc=models.CharField(max_length=50)
    lc=models.CharField(max_length=50)
    decision=models.CharField(max_length=50)
    mission=models.CharField(max_length=50)
    salaire=models.CharField(max_length=50)
    facture=models.CharField(max_length=50)
    datesaisie=models.DateField(max_length=50)
    datevalidation=models.DateField(max_length=50)
    database_name_gendata=models.CharField(max_length=50)
    virement_id=models.ForeignKey(Virement, on_delete=models.CASCADE, null=True, db_column='virement_id')
    idboncommande=models.ForeignKey(Boncommande, on_delete=models.CASCADE, null=True, db_column='idboncommande')
    idordre_payement=models.ForeignKey(Ordre_payement, on_delete=models.CASCADE, null=True, db_column='idordre_payement')
    class Meta:
        db_table = 'payement'  

    def __str__(self):
        return self.nom

class Periodes(models.Model):
    idperiodes=models.CharField(primary_key=True, null=False)
    libelle=models.CharField(max_length=50)
    rang=models.CharField(max_length=50)
    typeperiode_id=models.ForeignKey(Typeperiode, on_delete=models.CASCADE, null=True, db_column='typeperiode_id')
    class Meta:
        db_table = 'periodes'  

    def __str__(self):
        return self.nom

class Periodetaches(models.Model):
    idperiodetaches=models.CharField(primary_key=True, null=False)
    tache_id=models.ForeignKey(Tache, on_delete=models.CASCADE, null=True, db_column='tache_id')
    periode_id=models.ForeignKey(Periode, on_delete=models.CASCADE, null=True, db_column='periode_id')
    valeurrealisee=models.CharField(max_length=50)
    class Meta:
        db_table = 'periodetaches'  

    def __str__(self):
        return self.nom

class Performance(models.Model):
    idperformance=models.CharField(primary_key=True, null=False)
    justification=models.CharField(max_length=100)
    annepta=models.CharField(max_length=50)
    sourceverification=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    baseline=models.CharField(max_length=50)
    conditionreussite=models.CharField(max_length=50)
    sourecverifiactionanterieur=models.CharField(max_length=50)
    cibleanterieur=models.CharField(max_length=50)
    reductionecart=models.CharField(max_length=50)
    ecart=models.CharField(max_length=50)
    objectifspecifique=models.CharField(max_length=50)
    confditionreussite=models.CharField(max_length=100)
    enonceprojet=models.CharField(max_length=50)
    actioncorrectrices=models.CharField(max_length=50)
    conclusion=models.CharField(max_length=50)
    recommandation=models.CharField(max_length=50)
    criteresvalidation=models.CharField(max_length=50)
    valeurealise=models.CharField(max_length=50)
    observations=models.CharField(max_length=50)
    baselineanterieur=models.CharField(max_length=50)
    idindicateurperformance=models.ForeignKey(Indicateurperformance, on_delete=models.CASCADE, null=True, db_column='idindicateurperformance')
    idstructure=models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, db_column='idstructure')
    idmission=models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, db_column='idmission')
    idactivite=models.ForeignKey(Activite, on_delete=models.CASCADE, null=True, db_column='idactivite')
    class Meta:
        db_table = 'performance'  

    def __str__(self):
        return self.nom

class Rubriquedifficulte(models.Model):
    idrubriquedifficulte=models.CharField(primary_key=True, null=False)
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    class Meta:
        db_table = 'rubriquedifficulte'  

    def __str__(self):
        return self.nom

class Revue(models.Model):
    idrevue=models.CharField(primary_key=True, null=False)
    idannee=models.ForeignKey(Annee, on_delete=models.CASCADE, null=True, db_column='idannee')
    nom=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    class Meta:
        db_table = 'revue'  

    def __str__(self):
        return self.nom

class Revueactivite(models.Model):
    idrevueactivite=models.CharField(primary_key=True, null=False)
    activites=models.CharField(max_length=50)
    cout=models.CharField(max_length=50)
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True, db_column='idrevue')
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    observations=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    class Meta:
        db_table = 'revueactivite'  

    def __str__(self):
        return self.nom

class Revuefait(models.Model):
    idrevuefait=models.CharField(primary_key=True, null=False)
    fait=models.CharField(max_length=50)
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True, db_column='idrevue')
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    observations=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    implications=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    class Meta:
        db_table = 'revuefait'  

    def __str__(self):
        return self.nom

class Revueprogramme(models.Model):
    idrevueprogramme=models.CharField(primary_key=True, null=False)
    fait=models.CharField(max_length=50)
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True, db_column='idrevue')
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    observations=models.CharField(max_length=50)
    cout=models.CharField(max_length=50)
    produits=models.CharField(max_length=50)
    contextmeo=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    difficultes=models.CharField(max_length=50)
    prisencompte=models.CharField(max_length=50)
    ajustementactions=models.CharField(max_length=50)
    implications=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    class Meta:
        db_table = 'revueprogramme'  

    def __str__(self):
        return self.nom

class Revueperformance(models.Model):
    idrevueperformance=models.CharField(primary_key=True, null=False)
    tauxrealise=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    indicateur=models.CharField(max_length=50)
    valeurcible=models.CharField(max_length=50)
    valeurrealise=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True, db_column='idrevue')
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    class Meta:
        db_table = 'revueperformance'  

    def __str__(self):
        return self.nom

class Revuedifficilte(models.Model):
    idrevuedifficulte=models.CharField(primary_key=True, null=False)
    difficulte=models.CharField(max_length=50)
    solution=models.CharField(max_length=50)
    observations=models.CharField(max_length=50)
    idrubriquedifficulte=models.ForeignKey(Rubriquedifficulte, on_delete=models.CASCADE, null=True, db_column='idrubriquedifficulte')
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True, db_column='idrevue')
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    etat=models.CharField(max_length=50)
    derniere_modif=models.CharField(max_length=50)
    date_enregistre=models.CharField(max_length=50)
    class Meta:
        db_table = 'revuedifficilte'  

    def __str__(self):
        return self.nom

class Revueaction(models.Model):
    idrevueaction=models.CharField(primary_key=True, null=False)
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True, db_column='idaction')
    idrevue=models.ForeignKey(Revue, on_delete=models.CASCADE, null=True, db_column='idrevue')
    activitesupprimes=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    class Meta:
        db_table = 'revueaction'  

    def __str__(self):
        return self.nom

class Indicateurextrant(models.Model):
    idindicateurextrant=models.CharField(primary_key=True, null=False)
    idindicateuractivite=models.ForeignKey(Indicateuractivite, on_delete=models.CASCADE, null=True, db_column='idindicateuractivite')
    idextrant=models.ForeignKey(Extrant, on_delete=models.CASCADE, null=True, db_column='idextrant')
    idaction=models.ForeignKey(Action, on_delete=models.CASCADE, null=True, db_column='idaction')
    cible=models.CharField(max_length=50)
    observation=models.CharField(max_length=50)
    class Meta:
        db_table = 'indicateurextrant'  

    def __str__(self):
        return self.nom

class Privilege(models.Model):
    idprivilege=models.CharField(primary_key=True, null=False)
    id_compte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True, db_column='id_compte')
    id_groupe_utilisateur=models.ForeignKey(Groupe_utilisateur, on_delete=models.CASCADE, null=True, db_column='id_groupe_utilisateur')
    configuration=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    class Meta:
        db_table = 'privilege'  

    def __str__(self):
        return self.nom

class Privilege_b(models.Model):
     idprivilege_b=models.CharField(primary_key=True, null=False)
     idmenu=models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, db_column='idmenu')
     idcompte=models.ForeignKey(Compte, on_delete=models.CASCADE, null=True, db_column='idcompte')
     class Meta:
        db_table = 'privilege_b'  

     def __str__(self):
        return self.nom


class Programme1(models.Model):
    idprogramme1=models.CharField(primary_key=True, null=False)
    nom=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    stratrgieprogramme=models.CharField(max_length=50)
    respomeo=models.CharField(max_length=50)
    cadremeo=models.CharField(max_length=50)
    impact=models.CharField(max_length=50)
    etat=models.CharField(max_length=50)
    derniere_modif=models.DateField(max_length=50)
    objectifs=models.CharField(max_length=50)
    objectifstrategique=models.CharField(max_length=50)
    fonction=models.CharField(max_length=50)
    indicateur=models.CharField(max_length=50)
    baseline=models.CharField(max_length=50)
    cible=models.CharField(max_length=50)
    date_enregistre=models.DateField(max_length=50)
    idprogramme=models.ForeignKey(Programme, on_delete=models.CASCADE, null=True, db_column='idprogramme')
    idsoussecteur=models.ForeignKey(Soussecteur, on_delete=models.CASCADE, null=True, db_column='idsoussecteur')
    idinstitution=models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, db_column='idinstitution')
    idaxestrategique=models.ForeignKey(Axestrategique, on_delete=models.CASCADE, null=True, db_column='idaxestrategique')
    class Meta:
        db_table = 'programme1'  

    def __str__(self):
        return self.nom
    























   



























    

    





   
    






    
    





    






    



    






    





                    
                                   
    








    




















