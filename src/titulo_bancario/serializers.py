from rest_framework import serializers
from .models import TituloBancario


class TituloBancarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TituloBancario
        fields = '__all__'

    def validate(self, data):
        if data['idtitulo'] not in ['USD', 'TRPV', 'TP', 'TID', 'THI', 'TESU', 'TEST', 'TESP', 'TESOROS', 'TESI']:
            raise serializers.ValidationError("El idtitulo no es valido")
        return data

    def validate_idtitulo(self, value):
        if TituloBancario.objects.filter(idtitulo=value).exists():
            raise serializers.ValidationError("El idtitulo ya existe")
        return value

    def create(self, validated_data):
        titulo = TituloBancario.objects.create(**validated_data)
        if titulo.idtitulo == 'USD':
            titulo.titulo = 'DOLAR'
        elif titulo.idtitulo == 'TRPV':
            titulo.titulo = 'TÍTULO DE PARTICIPACIÓN RENTA VARIABLE'
        elif titulo.idtitulo == 'TP':
            titulo.titulo = 'TITULO DE PARTICIPACIÓN'
        elif titulo.idtitulo == 'TID':
            titulo.titulo = 'TIDIS'
        elif titulo.idtitulo == 'THI':
            titulo.titulo = 'TITULOS HIPOTECARIOS'
        elif titulo.idtitulo == 'TESU':
            titulo.titulo = 'TES UVR'
        elif titulo.idtitulo == 'TEST':
            titulo.titulo = 'TES TRM'
        elif titulo.idtitulo == 'TESP':
            titulo.titulo = 'TES PESOS'
        elif titulo.idtitulo == 'TESOROS':
            titulo.titulo = 'BONOS DEL TESORO EEUU'
        elif titulo.idtitulo == 'TESI':
            titulo.titulo = 'TES IPC'
        titulo.save()
        return titulo


