"""
URL configuration for appLycee1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from rest_framework import routers
from EmploiDeTemps.urls import router as routeurEmplois
router=routers.DefaultRouter()
router.registry.extend(routeurEmplois.registry)
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/',include('EmploiDeTemps.urls')),
#     path('classe/',include("EmploiDeTemps.urls")),
#     path("enseignant_salle/<int:id>/",include("EmploiDeTemps.urls")),
#     path('coursSalle/<int:idClasse>/',include("EmploiDeTemps.urls"))
# ]
#from EmploiDeTemps.views import EnsView
urlpatterns= [
    path('admin/',admin.site.urls),
    #path('', include(router.urls)),
    path('', views.home, name='home'),
    path('timeTable/<int:idClasse>/',include("EmploiDeTemps.urls"))
]
