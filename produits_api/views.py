from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Produit
from .serializers import ProduitSerializer

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
