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

Se debe:
1- Informar cantidad de títulos registrados.
2- Solicitar al usuario el idtitulo de un título y registrar que ha pagado la cuota adeudada.
3- Modificar la fecha de creación de todos los título ingresados el 2022-01-25, para indicar que en realidad ingresaron el 2022-02-01.
4- Solicitar el idtitulo de un titulo y darlo de baja (eliminarlo del listado).
5- Imprimir el listado de títulos completo.
6- Se debe cumplir con las buenas prácticas, clean code, principios solid, y es requerido el manejo de pruebas unitarias


"""
from django.test import TestCase
from .models import TituloBancario
from .views import TituloPagoCuota, TituloBaja, TituloFecha, TituloLista, TituloDetalle

class TituloBancarioTestCase(TestCase):
    def setUp(self):
        TituloBancario.objects.create(
            idtitulo='USD',
            titulo='DOLAR',
            clasificacion='DIV',
            valor=500000000,
            fecha_creacion='2022-03-14',
            fecha_vencimiento='2023-03-15',
            pagocuota='y'
        )
        TituloBancario.objects.create(
            idtitulo='TRPV',
            titulo='TÍTULO DE PARTICIPACIÓN RENTA VARIABLE',
            clasificacion='DIV',
            valor=256000000,
            fecha_creacion='2022-08-25',
            fecha_vencimiento='2023-08-26',
            pagocuota='y'
        )
        TituloBancario.objects.create(
            idtitulo='TP',
            titulo='TITULO DE PARTICIPACIÓN',
            clasificacion='DIV',
            valor=360000000,
            fecha_creacion='2022-02-16',
            fecha_vencimiento='2023-02-17',
            pagocuota='y'
        )

    def test_titulo_bancario(self):
        titulo = TituloBancario.objects.get(idtitulo='USD')
        self.assertEqual(titulo.titulo, 'DOLAR')
        self.assertEqual(titulo.clasificacion, 'DIV')
        self.assertEqual(titulo.valor, 500000000)
        self.assertEqual(titulo.pagocuota, 'y')

    def test_titulo_pago_cuota(self):
        titulo = TituloBancario.objects.get(idtitulo='USD')
        titulo.pagocuota = 'n'
        self.assertEqual(titulo.pagocuota, 'n')

    def test_titulo_baja(self):
        titulo = TituloBancario.objects.get(idtitulo='USD')
        titulo.delete()
        self.assertEqual(titulo.idtitulo, 'USD')

    def test_titulo_fecha(self):
        titulo = TituloBancario.objects.get(idtitulo='USD')
        titulo.fecha_creacion = '2022-02-01'
        self.assertEqual(titulo.fecha_creacion, '2022-02-01')

    def test_titulo_lista(self):
        titulo = TituloBancario.objects.all()
        self.assertEqual(titulo.count(), 3)

    def test_titulo_detalle(self):
        titulo = TituloBancario.objects.get(idtitulo='USD')
        self.assertEqual(titulo.idtitulo, 'USD')
        self.assertEqual(titulo.titulo, 'DOLAR')
        self.assertEqual(titulo.clasificacion, 'DIV')
        self.assertEqual(titulo.valor, 500000000)
        self.assertEqual(titulo.pagocuota, 'y')







