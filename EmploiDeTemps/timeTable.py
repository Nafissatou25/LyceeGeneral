from .models import *

class emploiDeTemps():
    def __init__(self,idClasse):
        self.idClasse=idClasse
    def etablissement(self):
        query1=Classe.objects.filter(id=self.idClasse).all()
        data={}
        for i,elt in enumerate(query1):
            data[i]=elt.id_niveau.id_etablissement.__dict__['nom']
        return data
    def lesCours(self):
        query1=ClasseCours.objects.filter(id_classe=self.idClasse).all()
        cours={}
        lesSalles=[]
        for i,elt in enumerate(query1):
            cours[str(i)]=dict(elt.id_cours.__dict__)
            lesSalles.append(elt.id_cours.__dict__)
        for i in cours:
            for elt1 in cours[i]:
                del cours[i][elt1]
                break
        return cours,lesSalles
    def enseignant(self):
        query1=ClasseEnseignantCours.objects.filter(id_classe=self.idClasse).all()
        data={}
        for i,elt in enumerate(query1):
            data1={}
            data1["idProf"]=elt.id_enseignant.__dict__["id"]
            data1['nomProf']=elt.id_enseignant.__dict__["nom"]
            data1["gradeProf"]=elt.id_enseignant.__dict__["id_grade_id"]
            data1["idCours"]=elt.id_cours.__dict__["id"]
            data1['intituleCours']=elt.id_cours.__dict__["intitule"]
            data1["typeCours"]=elt.id_cours.id_typecours.__dict__["nom"]
            data1["idSalle"]=elt.id_cours.__dict__["id_salle_id"]#id_grade_id
            data[str(i+1)]=data1
        return data
    def periode(self):
        query1=ClassePeriodeCours.objects.filter(id_classe=self.idClasse).all()
        data={}
        for i,elt in enumerate(query1):
            data[str(i+1)]={}
            data[str(i+1)]["date_debut"]=elt.id_periode.__dict__["date_debut"]
            data[str(i+1)]["date_fin"]=elt.id_periode.__dict__["date_fin"]
            data[str(i+1)]["idJour"]=elt.id_periode.__dict__["id_jour_id"]
            data[str(i+1)]['IdCours']=elt.id_cours.__dict__["id"]
            data[str(i+1)]['IntituleCours']=elt.id_cours.__dict__["intitule"]
            data[str(i+1)]['TypeCours']=elt.id_cours.id_typecours.__dict__["nom"]
            #data[str(i+1)]["idCours"]=elt.id_cours.__dict__['id']
            #data[str(i+1)]["intitule"]=elt.id_cours.__dict__['intitule']
        return data  
    def lesSalles(self):
        salle=Salle.objects.filter(id=self.idClasse)
        query1=Salle.objects.filter(id__in=(salle)).all()
        data={}
        for i,elt in enumerate(query1):
            data[str(i)]={}
            data[str(i)]["classe"]=elt.nom
            data[str(i)]["ets"]=dict(elt.id_ets.__dict__["Nom"])
        return data
    
