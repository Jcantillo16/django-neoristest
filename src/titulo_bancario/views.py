from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TituloBancario
from .serializers import TituloBancarioSerializer


class TituloLista(APIView):
    def get(self, request):
        titulo = TituloBancario.objects.all()
        serializer = TituloBancarioSerializer(titulo, many=True)
        count = len(serializer.data)
        return Response({'count': count,
                         'titulo': serializer.data},
                        status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TituloBancarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TituloDetalle(APIView):
    def get_object(self, pk):
        try:
            return TituloBancario.objects.get(pk=pk)
        except TituloBancario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        titulo = self.get_object(pk)
        serializer = TituloBancarioSerializer(titulo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        titulo = self.get_object(pk)
        serializer = TituloBancarioSerializer(titulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        titulo = self.get_object(pk)
        titulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3- Modificar la fecha de creación de todos los título ingresados el 2022-01-25, para indicar que en realidad ingresaron el 2022-02-01.
class TituloFecha(APIView):
    def get(self, request):
        titulo = TituloBancario.objects.all()
        serializer = TituloBancarioSerializer(titulo, many=True)
        titulos_modificados = []
        for i in serializer.data:
            if i['fecha_creacion'] == '2022-01-25':
                i['fecha_creacion'] = '2022-02-01'
                titulos_modificados.append(i)
            else:
                return Response({'message': 'No se encontraron titulos con fecha de creacion 2022-01-25'},
                                status=status.HTTP_400_BAD_REQUEST)
        numero_titulos_modificados = len(titulos_modificados)
        return Response({'numero_titulos_modificados': numero_titulos_modificados,
                         'titulos_modificados': titulos_modificados, },
                        status=status.HTTP_200_OK)


# 4- Solicitar el idtitulo de un titulo y darlo de baja (eliminarlo del listado).
class TituloBaja(APIView):
    def get(self, request, idtitulo):
        titulo = TituloBancario.objects.filter(idtitulo=idtitulo)
        serializer = TituloBancarioSerializer(titulo, many=True)
        if serializer.data:
            titulo.update(idtitulo=idtitulo + '-BAJA')
            return Response({'message': 'El titulo con idtitulo ' + idtitulo + ' ha sido dado de baja'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No se encontraron titulos con idtitulo ' + idtitulo},
                            status=status.HTTP_400_BAD_REQUEST)


# 2- Solicitar al usuario el idtitulo de un título y registrar que ha pagado la cuota adeudada.
class TituloPagoCuota(APIView):
    def post(self, request):
        idtitulo = request.data['idtitulo']
        titulo = TituloBancario.objects.filter(idtitulo=idtitulo)
        serializer = TituloBancarioSerializer(titulo, many=True)
        if serializer.data:
            titulo.update(pagocuota='y')
            return Response({'message': 'El titulo con idtitulo ' + idtitulo + ' ha sido pagado'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No se encontraron titulos con idtitulo ' + idtitulo},
                            status=status.HTTP_400_BAD_REQUEST)
