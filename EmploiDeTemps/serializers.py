from .models import *
from rest_framework import serializers

class Ens(serializers.ModelSerializer):
    
    class Meta:
        model=Enseignant
        fields='__all__'

class Clas(serializers.ModelSerializer):
    
    class Meta:
        model=Classe
        fields='__all__'

class ClasPeriode(serializers.ModelSerializer):
    
    class Meta:
        model=ClassePeriodeCours
        fields='__all__'
class ClasEnsCours(serializers.ModelSerializer):
    
    class Meta:
        model=ClasseEnseignantCours
        fields='__all__'
class cours(serializers.ModelSerializer):
    
    class Meta:
        model=Cours
        fields='__all__'

class SalePer(serializers.ModelSerializer):
    
    class Meta:
        model=SallePeriode
        fields='__all__'
class Direc(serializers.ModelSerializer):
    
    class Meta:
        model=Directeur
        fields='__all__'
class EnsMatiere(serializers.ModelSerializer):
    
    class Meta:
        model=EnseignantMatiere
        fields='__all__'
class Ets(serializers.ModelSerializer):
    
    class Meta:
        model=Etablissement
        fields='__all__'
class Grad(serializers.ModelSerializer):
    
    class Meta:
        model=Grade
        fields='__all__'
class jours(serializers.ModelSerializer):
    
    class Meta:
        model=Jour
        fields='__all__'
class Mat(serializers.ModelSerializer):
    
    class Meta:
        model=Matiere
        fields='__all__'
class Senc(serializers.ModelSerializer):
    
    class Meta:
        model=Senceur
        fields='__all__'
class SalEns(serializers.ModelSerializer):
    
    class Meta:
        model=SalleEnseignant
        fields='__all__'
class Sal(serializers.ModelSerializer):
    
    class Meta:
        model=Salle
        fields='__all__'
class Niv(serializers.ModelSerializer):
    
    class Meta:
        model=Niveau
        fields='__all__'
class Peri(serializers.ModelSerializer):
    
    class Meta:
        model=Periode
        fields='__all__'
class TypCrs(serializers.ModelSerializer):
    
    class Meta:
        model=Typecours
        fields='__all__'
class ClasCrs(serializers.ModelSerializer):
    
    class Meta:
        model=ClasseCours
        fields='__all__'