from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Produit
from .serializers import ProduitSerializer

from .auth_serializers import EnregistrementUtilisateur
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class ProduitAPIView(APIView):
    # Récupérer tous les produits
    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

    # Créer un produit
    def post(self, request):
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Inscription utilisateur et création de compte utilisateur

class InscriptionUtilisateur(APIView):
    permission_classes = []  # Permettre l'accès sans authentification
    def post(self, request):
        # Serializer les données de la requête pour la création d'un nouvel utilisateur
        serializer = EnregistrementUtilisateur(data=request.data)
        # verifier si les données sont valides
        if serializer.is_valid():
            utilisateur = serializer.CreerUtilisateur(serializer.validated_data)
            # retourner une réponse de succès 201 Created
            return Response({
                "status": "success",
                "nomUtilisateur": utilisateur.username,
                "message": "Utilisateur créé avec succès"}, status=status.HTTP_201_CREATED)
        # retourner une réponse d'erreur 400 Bad Request avec les erreurs de validation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Connexion utilisateur et génération de token d'authentification

class ConnexionUtilisateur(APIView):
    permission_classes = []  # Permettre l'accès sans authentification
    def post(self, request):
        nomUtilisateur = request.data.get('username')
        motDePasse = request.data.get('password')
        utilisateur = authenticate(username=nomUtilisateur, password=motDePasse)
        if utilisateur:
            token, created = Token.objects.get_or_create(user=utilisateur)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Nom d'utilisateur ou mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)
