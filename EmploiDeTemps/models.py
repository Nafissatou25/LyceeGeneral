# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Classe(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    nom_classe = models.CharField(unique=True, max_length=20)
    nombre_heure_semaine = models.IntegerField()
    description = models.TextField(null=True)
    id_niveau = models.ForeignKey('Niveau', models.DO_NOTHING, db_column='id_Niveau')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'classe'


class ClassePeriodeCours(models.Model):
    id_classe = models.OneToOneField(Classe, models.DO_NOTHING, db_column='id_Classe', primary_key=True)  # Field name made lowercase. The composite primary key (id_Classe, id_Periode, id_Cours) found, that is not supported. The first column is selected.
    id_periode = models.ForeignKey('Periode', models.DO_NOTHING, db_column='id_Periode', blank=True)  # Field name made lowercase.
    id_cours = models.ForeignKey('Cours', models.DO_NOTHING, db_column='id_Cours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'classe_periode_cours'


class Cours(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess
    intitule = models.CharField(max_length=30, blank=True, null=True)
    heure_cours_semaine = models.IntegerField(blank=True, null=True)
    id_typecours = models.ForeignKey('Typecours', models.DO_NOTHING, db_column='id_typeCours', blank=True, null=True)  # Field name made lowercase.
    id_salle=models.ForeignKey('Salle',models.DO_NOTHING,db_column="id_salle",default=0)
    class Meta:
        managed = True
        db_table = 'cours'
class ClasseCours(models.Model):
    id_classe=models.ForeignKey('Classe',models.DO_NOTHING,db_column="id_classe")
    id_cours=models.ForeignKey('Cours',models.DO_NOTHING,db_column='id_cours')
    class Meta:
        managed=True
        db_table='classe_cours'
class SallePeriode(models.Model):
    id_periode=models.ForeignKey('Periode',models.DO_NOTHING,db_column='id_periode')
    id_salle=models.ForeignKey("Salle",models.DO_NOTHING,db_column="id_salle")
    
class Directeur(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    nom = models.CharField(max_length=20, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    login = models.CharField(unique=True, max_length=20, blank=True, null=True)
    password = models.CharField(unique=True, max_length=20, blank=True, null=True)
    id_ets = models.ForeignKey('Etablissement', models.DO_NOTHING, db_column='id_ets', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Directeur'


class Enseignant(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    nom = models.CharField(max_length=30, blank=True, null=True)
    prenom = models.CharField(max_length=25, blank=True, null=True)
    heure_cours_semaine = models.IntegerField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=20, blank=True, null=True)
    password = models.CharField(unique=True, max_length=20, blank=True, null=True)
    id_grade = models.ForeignKey('Grade', models.DO_NOTHING, db_column='id_grade', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enseignant'


class EnseignantMatiere(models.Model):
    id_enseignant = models.OneToOneField(Enseignant, models.DO_NOTHING, db_column='id_Enseignant', primary_key=True)  # Field name made lowercase. The composite primary key (id_Enseignant, id_Matiere) found, that is not supported. The first column is selected.
    id_matiere = models.ForeignKey('Matiere', models.DO_NOTHING, db_column='id_Matiere', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'enseignant_matiere'


class Etablissement(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    nom = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'etablissement'


class Grade(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    grade = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'grade'


class Jour(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    jour = models.CharField(max_length=20,unique=True)

    class Meta:
        managed = True
        db_table = 'jour'


class Matiere(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    matiere = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'matiere'


class Niveau(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    niveau = models.IntegerField(unique=True, blank=True, null=True)
    id_etablissement = models.ForeignKey(Etablissement, models.DO_NOTHING, db_column='id_Etablissement', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'niveau'


class Periode(models.Model):
    id = models.IntegerField(primary_key=True,)  # This field type is a guess.
    date_debut = models.IntegerField(blank=True, null=True)
    date_fin = models.IntegerField(blank=True, null=True)
    id_jour = models.ForeignKey(Jour, models.DO_NOTHING, db_column='id_Jour', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'periode'


class Salle(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    nom = models.CharField(unique=True, max_length=20, blank=True, null=True)
    id_ets=models.ForeignKey('Etablissement',models.DO_NOTHING,db_column="id_departement",default=0)

    class Meta:
        managed = True
        db_table = 'salle'


class SalleEnseignant(models.Model):
    id_enseignant = models.OneToOneField(Enseignant, models.DO_NOTHING, db_column='id_Enseignant', primary_key=True)  # Field name made lowercase. The composite primary key (id_Enseignant, id_Salle, id_Cours) found, that is not supported. The first column is selected.
    id_salle = models.ForeignKey(Salle, models.DO_NOTHING, db_column='id_Salle', blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        managed = True
        db_table = 'salle_enseignant'


class Senceur(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    nom = models.CharField(max_length=20, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    login = models.CharField(unique=True, max_length=20, blank=True, null=True)
    password = models.CharField(unique=True, max_length=20, blank=True, null=True)
    id_niveau = models.ForeignKey(Niveau, models.DO_NOTHING, db_column='id_Niveau', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'senceur'


class Typecours(models.Model):
    id = models.IntegerField(primary_key=True)  # This field type is a guess.
    nom = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = True
        db_table = 'typecours'
