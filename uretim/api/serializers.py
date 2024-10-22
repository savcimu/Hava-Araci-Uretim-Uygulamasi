from rest_framework import serializers
from ..models import Parca, Ucak, UretilenUcak, Personel, Takim

class ParcaSerializer(serializers.ModelSerializer):
    ureten_personel = serializers.StringRelatedField()

    class Meta:
        model = Parca
        fields = ['id', 'ucak', 'parca_tipi', 'ureten_personel']

class UcakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ucak
        fields = ['id', 'ad']

class UretilenUcakSerializer(serializers.ModelSerializer):
    kullanilan_parcalar = ParcaSerializer(many=True)
    ureten_personel = serializers.StringRelatedField()

    class Meta:
        model = UretilenUcak
        fields = ['id', 'ucak_tipi', 'kullanilan_parcalar', 'ureten_personel', 'tarih']

class PersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personel
        fields = ['id', 'user', 'takim']

class TakimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Takim
        fields = ['id', 'takim_tipi']
