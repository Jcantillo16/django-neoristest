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












