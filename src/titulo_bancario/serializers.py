"""
- Crear un programa para gestionar datos de los títulos bancarios, permitiendo:

- Cargar información de los títulos en un diccionario para acceder por número de título.

Los datos a almacenar son: idtitulo, titulo,clasificación,valor, fecha de creación (aaaammdd), fecha vencimiento (aaaammdd), pagocuota (y/n)

El programa debe iniciar con 3 datos de los títulospreestablecidos ya cargados:

Título nº1, USD, DOLAR, DIV, 500.000.000, 2022-03-14, 2023-03-15,’y’
Titulo nº2, TRPV, TÍTULO DE PARTICIPACIÓN RENTA VARIABLE: 256.000.000, 2022-08-25, 2023-08-26,’y’
Título nº3, TP,TITULO DE PARTICIPACIÓN,360.000.000,2022-02-16, 2023-02-17,’y’

Tomar en cuenta:

.- El idtitulo sólo puede tener como valor:
USD,TRPV,TP,TID,THI,TESU,TEST,TESP,TESOROS,TESI
No se debe repetir.

.- El título sólo puede tener como valor:
DOLAR,TÍTULO DE PARTICIPACIÓN RENTA VARIABLE,TITULO DE PARTICIPACIÓN,TIDIS,TITULOS HIPOTECARIOS,TES UVR,TES TRM,TES PESOS,BONOS DEL TESORO EEUU,TES IPC

"""
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


