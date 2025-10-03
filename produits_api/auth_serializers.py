from django.contrib.auth.models import User
from rest_framework import serializers

class EnregistrementUtilisateur(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True)
    password= serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def CreerUtilisateur(self, BodyCorrect):
        utilisateur = User.objects.create_user(
            username=BodyCorrect['username'],
            password=BodyCorrect['password']
        )
        return utilisateur