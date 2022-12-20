"""
 Crear un programa para gestionar datos de los títulos bancarios, permitiendo:

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
from django.db import models


# Create your models here.

class TituloBancario(models.Model):
    idtitulo = models.CharField(max_length=4)
    titulo = models.CharField(max_length=100, null=True, blank=True )
    clasificacion = models.CharField(max_length=100)
    valor = models.IntegerField()
    fecha_creacion = models.DateField()
    fecha_vencimiento = models.DateField()
    pagocuota = models.CharField(max_length=1)

    class Meta:
        db_table = 'titulo_bancario'

    def __str__(self):
        return f"""
        idtitulo: {self.idtitulo}
        titulo: {self.titulo}
        clasificacion: {self.clasificacion}
        valor: {self.valor}
        fecha_creacion: {self.fecha_creacion}
        fecha_vencimiento: {self.fecha_vencimiento}
        pagocuota: {self.pagocuota}
        """


    def __repr__(self):
        return f"""
        idtitulo: {self.idtitulo}
        titulo: {self.titulo}
        clasificacion: {self.clasificacion}
        valor: {self.valor}
        fecha_creacion: {self.fecha_creacion}
        fecha_vencimiento: {self.fecha_vencimiento}
        pagocuota: {self.pagocuota}
        """



