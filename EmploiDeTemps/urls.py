from django.urls import path
from  . import views as view
from rest_framework import routers
# urlpatterns = [
#     path('classe/',obtenirLesClasses,name="classe"),
#     path('enseignant/',enseigant_salle,name="enseignant_salle"),
#     path('etPeriode/',cours,name='coursPeriode')
# ]
urlpatterns = [
    path("EmploisDeTemps/",view.emploiDeTemp,name="Emplois de teps")
]
router=routers.DefaultRouter()
router.register(r'Ens',view.SerialEns,basename='ens')
router.register(r'ClasseEnseignantCours',view.SerialClasseEnseignantCours,basename='ClasseEnseignantCours')
router.register(r'ClasseCoursPeriode',view.SerialClassePeriode,basename='ClasseCoursPeriode')
router.register(r'Cours',view.SerialCours,basename='Cours')
router.register(r'Ets',view.SerialEtablissement,basename='Ets')
router.register(r'Periode',view.SerialPeriode,basename='Periode')
router.register(r'Salle',view.SerialSalle,basename='Salle')
router.register(r'Jours',view.SerialJours,basename='Jours')
router.register(r'Directeur',view.SerialDirecteur,basename='Directeur')
router.register(r'ClasseEtCours',view.SerialClasseCours,basename='ClasseEtCours')

