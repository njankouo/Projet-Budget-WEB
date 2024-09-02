# tutorial/forms.py
from django import forms
from .models import Tache

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = [
            'nom', 'numordre', 'totalmontantaloue', 'moyensnecessaires', 'indicateurs2014',
            'aeencours', 'cpconsommee', 'indicateurspoursuivis', 'valider', 'm1', 'etat',
            'm2', 'date_enregistre', 'derniere_modif', 'periodeexecution', 'montantengage',
            'montantliquide', 'montantpayeht', 'montantpayettc', 'resultprocess', 'indicateurresult',
            'montant_ordonne', 'taxe_ordonne', 'nap_ordonne', 'valeurattendue', 'justification',
            'valeurrealisee', 'cpanneeplus1', 'cpanneeplus2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9',
            'm10', 'm11', 'm12', 'idevaluationstructure', 'periode_id', 'idannee', 'idnaturetache',
            'idnature_t', 'idbailleurfond', 'idstructure', 'idrisque', 'idactivite', 'idtypefinancement'
        ]
