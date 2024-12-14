
from django.http import JsonResponse
from . import serializers as serial
from . import models as model
from .timeTable import emploiDeTemps
import json
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import viewsets,status

#Vue des Enseignants
class SerialEns(viewsets.ModelViewSet):
    serializer_class=serial.Ens
    queryset=model.Enseignant.objects.all()
#Vue des Salles de classe
class SerialSalleDeClasse(viewsets.ModelViewSet):
    serializer_class=serial.Clas
    queryset=model.Classe.objects.all()
#Vues des Classes Enseignants et des cours
class SerialClasseEnseignantCours(viewsets.ModelViewSet):
    serializer_class=serial.ClasEnsCours
    queryset=model.ClasseEnseignantCours.objects.all()
#Vues des Classes Cours
class SerialClasseCours(viewsets.ModelViewSet):
    serializer_class=serial.ClasseCours
    queryset=model.ClasseCours.objects.all()

# Vues Classe Periode Cours
class SerialClassePeriode(viewsets.ModelViewSet):
    serializer_class=serial.ClasPeriode
    queryset=model.ClassePeriodeCours.objects.all()
# Vues des cours
class SerialCours(viewsets.ModelViewSet):
    serializer_class=serial.cours
    queryset=model.Cours.objects.all()
# Vues 
class SerialDirecteur(viewsets.ModelViewSet):
    serializer_class=serial.Direc
    queryset=model.Directeur.objects.all()

class SerialEnsMat(viewsets.ModelViewSet):
    serializer_class=serial.EnsMatiere
    queryset=model.EnseignantMatiere.objects.all()

class SerialSalle(viewsets.ModelViewSet):
    serializer_class=serial.Sal
    queryset=model.Salle.objects.all()

class SerialEtablissement(viewsets.ModelViewSet):
    serializer_class=serial.Ets
    queryset=model.Etablissement.objects.all()

class SerialGrade(viewsets.ModelViewSet):
    serializer_class=serial.Grad
    queryset=model.Grade.objects.all()
    
class SerialPeriode(viewsets.ModelViewSet):
    serializer_class=serial.Peri
    queryset=model.Periode.objects.all()
    
class SerialJours(viewsets.ModelViewSet):
    serializer_class=serial.jours
    queryset=model.Jour.objects.all()
class SerialTypeCours(viewsets.ModelViewSet):
    serializer_class=serial.TypCrs
    queryset=model.Typecours.objects.all()

class SerialClasseCours(viewsets.ModelViewSet):
    serializer_class=serial.ClasCrs
    queryset=model.ClasseCours.objects.all()
# class SerialClasseEnseignantCours(viewsets.ModelViewSet):
#     serializer_class=serial.ClasEnsCours
#     queryset=model.ClasseEnseignantCours.objects.all()
# class SerialClasseEnseignantCours(viewsets.ModelViewSet):
#     serializer_class=serial.ClasEnsCours
#     queryset=model.ClasseEnseignantCours.objects.all()

def emploiDeTemp(request,idClasse,**args):
    emp=emploiDeTemps(idClasse)
    dicEts=emp.etablissement()
    #dicCours,dicSalle=emp.lesCours()
    dicEnseCours=emp.enseignant()
    dicPeriode=emp.periode()
    data={"ets":dicEts,"EnseignantEtCours":dicEnseCours,"PeriodeEtCours":dicPeriode}
    return JsonResponse(data)