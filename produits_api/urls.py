from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProduitAPIView
from .views import InscriptionUtilisateur, ConnexionUtilisateur




urlpatterns = [
    path('produits/', ProduitAPIView.as_view(), name='produit-list'),
    path('inscription/', InscriptionUtilisateur.as_view(), name='inscription'),
    path('connexion/', ConnexionUtilisateur.as_view(), name='connexion'),
]