from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ProduitViewSet
from .views import ProduitAPIView


# router = DefaultRouter()
# router.register(r'produits', ProduitViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
urlpatterns = [
    path('produits/', ProduitAPIView.as_view(), name='produit-list'),
]